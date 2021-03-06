# !/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
# @Author:       wangwei
# @E-mail:        wangwei03@gyyx.cn
# @Create Date:  2012-10-23
# @Version:      V6
##############################################################################
import paramiko, os, sys, datetime, time, MySQLdb


def log_w(text):
    logfile = "/home/create_slave.log"
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    tt = str(now) + "\t" + str(text) + "\n"
    f = open(logfile, 'a+')
    f.write(tt)
    f.close()


class Database:
    def __init__(self, host):
        self.user = 'root'
        self.password = '123456'
        self.port = 22
        self.today = datetime.date.today().strftime('%Y%m%d')
        self.binlogdir = '/data1/mysql_log'
        self.host = host
        if not os.path.isdir(self.binlogdir):
            os.makedirs(self.binlogdir)
            os.popen("ln -s /data1/mysql_log /mysql_log")
        if not os.path.isdir('/data1/mysql_log/binlog'):
            os.makedirs('/data1/mysql_log/binlog')
        if not os.path.isdir('/data1/mysql_log/relaylog'):
            os.makedirs('/data1/mysql_log/relaylog')
        os.popen("chown -R mysql.mysql /data1/mysql_log/")

    def check_mysql(self):  # 检查从库nysql数据库服务是否运行，如在运行则pkill掉，然后跳过权限表启动，为导入数据做准备
        text = "Check mysql now,Please wait...."
        log_w(text)
        print "\033[1;32;40m%s\033[0m" % text
        os.popen("rm -rf /mysql_log/binlog/* && rm -rf /mysql_log/relaylog/*")
        if not os.path.isdir("/usr/local/mysql"):
            text = "    Mysql not install,Please install mysql !"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit()
        if os.popen("netstat -ntlp|grep 3306|wc -l").read().strip() != '0':
            os.popen("pkill mysqld")
        while 1:
            if os.popen("netstat -ntlp|grep 3306|wc -l").read().strip() == '0':
                for f in os.listdir("/home/mysql/data"):  # 清空此目录中除mysql目录之外的所有文件和目录
                    if f != 'mysql':
                        os.popen("rm -rf /home/mysql/data/%s" % f)
                conm = "/usr/local/mysql/bin/mysqld_safe --defaults-file=/usr/local/mysql/etc/innodb.cnf --datadir=/home/mysql/data --user=mysql --skip-grant-tables &"
                os.popen(conm)
                break
            else:
                text = "Mysql not stop,please wait..."
                log_w(text)
                print text
                time.sleep(5)
        time.sleep(20)
        if os.popen("netstat -ntlp|grep 3306|wc -l").read().strip() == '0':
            text = "Mysql not Running,please start with '--skip-grant-tables' !"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit()

    def export_table(self):  # 导出当前主库的表结构
        print "\033[1;32;40m%s\033[0m" % "Export master table and back mysql,Please wait ...."
        try:
            s = paramiko.SSHClient()
            s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            s.connect(self.host, self.port, self.user, self.password)
            conm = "/usr/local/mysql/bin/mysqldump --add-drop-table -udump -p123456 -d -A|bzip2 -2 > /data/script/db_back/table_%s.bz2 && cp -f /usr/local/mysql/etc/innodb.cnf /data/script/db_back/ && echo $?" % self.today
            stdin, stdout, stderr = s.exec_command(conm)
            result = stdout.readlines()[-1].strip()
            s.close()
            if result == '0':
                text = "    Export_table success !"
                log_w(text)
                print text
            else:
                text = "Export_table Error !"
                log_w(text)
                print "\033[1;31;40m%s\033[0m" % text
                sys.exit()
        except Exception, e:
            text = "SSH connect Error !"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit()

    def down_back(self):  # 拷贝主库当天的数据库备份和表结构
        local_dir = '/data1/'
        remote_dir = '/data/script/db_back/'
        try:
            t = paramiko.Transport((self.host, self.port))
            t.connect(username=self.user, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(t)
            files = sftp.listdir(remote_dir)
            text = "Download back file,Please wait ...."
            log_w(text)
            print "\033[1;32;40m%s\033[0m" % text
            text = '    Beginning to download file  from %s  %s ' % (self.host, datetime.datetime.now())
            log_w(text)
            print text
            for f in files:
                if f.find(self.today) != -1 or f == 'innodb.cnf':
                    text = "        Downloading file:%s:%s" % (self.host, os.path.join(remote_dir, f))
                    log_w(text)
                    print text
                    sftp.get(os.path.join(remote_dir, f), os.path.join(local_dir, f))
                    # sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))
            t.close()
            text = '    Download All back file success %s ' % datetime.datetime.now()
            log_w(text)
            print text
        except Exception, e:
            text = "SFTP connect Error !"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit()

    def unbz2(self):  # 解压拷贝的数据库备份和表结构bz2包
        text = "Decompression file,Please wait ...."
        log_w(text)
        print "\033[1;32;40m%s\033[0m" % text
        text = '    Beginning to Decompression file  from %s' % datetime.datetime.now()
        log_w(text)
        print text
        conm = 'bzip2 -dfk /data1/*%s*.bz2 && echo $?' % self.today
        bz = os.popen(conm).read().strip()
        if bz == '0':
            text = '    Decompression file  success %s' % datetime.datetime.now()
            log_w(text)
            print text
        else:
            text = "Decompression Error !"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit()

    def restart_mysql(self):
        text = "Restart mysql Now,Please wait ...."
        log_w(text)
        print "\033[1;32;40m%s\033[0m" % text
        os.popen("rm -rf /usr/local/mysql/etc/innodb.cnf && cp -f /data1/innodb.cnf /usr/local/mysql/etc/innodb.cnf")
        old_id = os.popen("cat /usr/local/mysql/etc/innodb.cnf |grep ^server-id|awk '{print $3}'").read().strip()
        new_id = int(old_id) + 1
        os.popen(
            "sed -i 's/server-id       = %s/server-id       = %s/' /usr/local/mysql/etc/innodb.cnf" % (old_id, new_id))
        os.popen("/usr/local/mysql/bin/mysqladmin shutdown")
        os.popen("rm -rf /home/mysql/data/*.info && rm -rf /home/mysql/data/ib_logfile*")
        os.popen(
            "/usr/local/mysql/bin/mysqld_safe --defaults-file=/usr/local/mysql/etc/innodb.cnf --datadir=/home/mysql/data --user=mysql &")
        time.sleep(20)
        if os.popen("netstat -ntlp|grep 3306|wc -l").read().strip() == '0':
            text = "Mysql restart Error,please check!"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit()

    def import_date(self):  # 导入表结构和备份数据库
        text = "Slave import master date,Please wait ...."
        log_w(text)
        print "\033[1;32;40m%s\033[0m" % text
        # 导入表结构
        dir = '/data1/'
        table = 'table_%s' % self.today
        conm = "/usr/local/mysql/bin/mysql  < %s%s && echo $?" % (dir, table)
        result = os.popen(conm).read().strip()
        if result == '0':
            text = "    Import %s success !" % table
            log_w(text)
            print text
        else:
            text = "Import Table structure Error !"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit()

        for f in os.listdir(dir):  # 导入数据库
            if os.path.isfile(os.path.join(dir, f)) and (f.find('bz2') == -1) and (f.find('table') == -1):
                if f.find('wd') != -1 and f.find(self.today) != -1:
                    conm = "/usr/local/mysql/bin/mysql < %s && echo $?" % os.path.join(dir, f)
                    result = os.popen(conm).read().strip()
                    if result == '0':
                        text = "    Import %s success !" % f
                        log_w(text)
                        print text
                    else:
                        text = "Import Database adb Error !"
                        log_w(text)
                        print "\033[1;31;40m%s\033[0m" % text
                        sys.exit()

    def slave_start(self):  # 启动salve
        text = "Settings Slave,Please wait ...."
        log_w(text)
        print "\033[1;32;40m%s\033[0m" % text
        binlog, log_pos = self.bin_pos()
        sql = "change master to master_host='%s',master_user='repl',master_password='123456',master_port=3306,master_log_file='%s',master_log_pos=%s;" % (
        self.host, binlog, log_pos)
        try:
            conn = MySQLdb.connect(host='127.0.0.1', user='repl_monitor', passwd='123456', connect_timeout=5)
            cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            # cursor.execute("slave stop;")
            cursor.execute(sql)
            cursor.execute("slave start;")
            cursor.execute("show slave status;")
            alldata = cursor.fetchall()[0]
            if alldata["Slave_IO_Running"] == "Yes" and alldata["Slave_SQL_Running"] == "Yes":
                text = "    Settings Slave success!"
                log_w(text)
                print "\033[1;32;40m%s\033[0m" % text
                for key in alldata:
                    print "%21s :" % key + '\t' + str(alldata[key])
                time.sleep(5)
                print
                print "******************************************"
                print
                cursor.execute("show slave status;")
                alldata = cursor.fetchall()[0]
                for key in alldata:
                    print "%21s :" % key + '\t' + str(alldata[key])
            else:
                text = "    Settings Slave Error,Please check it!"
                log_w(text)
                print "\033[1;31;40m%s\033[0m" % text
            cursor.close()
            conn.close()
        except MySQLdb.Error, e:
            log_w(e)
            print e
            sys.exit()

    def bin_pos(self):  # 获取主库备份前的一个bin-log文件以及它的第一个pos位置
        dir = '/data1/'
        for f in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, f)) and (f.find('bz2') == -1) and (f.find('table') == -1):
                if f.find('wd') != -1 and f.find(self.today) != -1:
                    binlog = f.split('_')[3]
                    log_pos = f.split('_')[4]
                    return binlog, log_pos


def find_ip():  # 走中心应用确认本服务器是否用于从库
    text = "正在从中心应用确认本服务器是否用于从库，稍等......".decode("utf-8").encode("GBK")
    log_w(text)
    print "\033[1;32;40m%s\033[0m" % text
    ip = os.popen("cat /etc/sysconfig/network-scripts/ifcfg-eth0|grep IPADDR |awk -F '=' '{print $2}'").read().strip()
    try:
        conn = MySQLdb.connect(host='192.168.1.110', user='root', passwd='1q2w3e4r', connect_timeout=5)
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT c.dist_id,c.ip,c.app_name FROM center_app.main_category a, center_app.sub_category b, center_app.app_info c WHERE a.id = b.main_id AND b.dist_id = c.dist_id AND b.main_id = c.main_id AND b.main_id='2' AND c.app_name IN ('ldb','adb','slave') AND c.flag='1' AND c.del_info!=0 AND c.dist_id NOT IN ('0','1','-100','-1','222') AND c.ip='%s'" % ip
        cursor.execute(sql)
        alldata = cursor.fetchall()[0]
        if alldata["app_name"] == "slave":
            text = "    This server is slave server,server OK !!"
            log_w(text)
            print "\033[1;32;40m%s\033[0m" % text
        else:
            text = "    This server is not used slave server,server Error,please check it !!"
            log_w(text)
            print "\033[1;31;40m%s\033[0m" % text
            sys.exit
        cursor.close()
        conn.close()
    except MySQLdb.Error, e:
        log_w(e)
        print e
        sys.exit()


if __name__ == "__main__":
    print "\033[1;31;40m%s\033[0m" % '''''  
注意事项：1、确认主库已经按照要求修改配置文件打开了bin-log，设置了相关参数  
          2、确认从库已经安装和主库一样版本的mysql  
          3、确认从库的配置文件注释掉了log-bin，否则从库导入数据库时会出错  
          4、脚本运行过程中会清除从库/home/mysql/data/目录下面除mysql目录之外的所有目录和文件，有必要的话请做好备份  
          5、运行之后删除/data1/目录下的压缩包  
          6、运行格式：python create_slave.py 根据提示输入主库的内网地址  
          7、从库创建完成并且数据与主库追齐之后要用脚本验证数据的一致性，数据一致后整个创建从库过程完成  
          8、在执行check_mysql时，会出现Broken pipe的错误，这个是由于python调用系统命令关闭和打开mysql时显示的信息没有正确的显示在终端造成的，没有影响，暂时没有找到不让显示此类信息的方法，亟待解决  
'''.decode("utf-8").encode("GBK")
    find_ip()
    master_ip = raw_input('Enter :Mater_eth1_ip :')
    boss = Database(master_ip)
    boss.check_mysql()
    boss.export_table()
    boss.down_back()
    boss.unbz2()
    boss.import_date()
    boss.restart_mysql()
    boss.slave_start()