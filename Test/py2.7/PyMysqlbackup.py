#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :PyMysqlbackup.py
# Description      :
# Author         :Devon
# Date          :2018/3/21
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

# Import required python libraries
import os
import time
import datetime
import pipes


# 备份信息变量
DB_HOST = 'your_mysql_host' #ie. localhost
DB_USER = 'your_user_name'
DB_USER_PASSWORD = 'your_password'
#DB_NAME = '/backup/dbnames.txt'
DB_NAME = 'your_db_name'
BACKUP_PATH = '/tmp/'
conf_file = '/etc/my.cnf'
port = '3306'
bak_user = 'dbabackup'
bak_pwd = '123123'
check_status = 'netstat -lnt | grep %s | wc -l '%(port)

# 检查数据库状态
mysql_status = os.popen(check_status).read()
if mysql_status.strip() == '1':   # 命令执行成功返回0，否则返回1
    print 'mysql is running'
else:
    print 'mysql is not runing,you need start mysql before continue.'



#备份路径
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + DATETIME
# Checking if backup folder already exists or not. If not exists will create it.
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

# 检查备份软件是否安装
inno_path = os.system('which innobackupex')
inno_cmd = "innobackupex"
if inno_path == 0:
    print 'congratulate,innobackex have been installed,continue.'
else:
    print 'the innobackpex tool is not been installed, you need install it to continue.'

b = os.popen('which innobackupex')  # 这里b只能调用一次。
# print b.read().split('/')[-1].replace('\n', '') == 'ls':
if b.read().split('/')[-1].replace('\n', '') == 'innobackupex':
    print 'sucess'
    inno_cmd = os.popen('which innobackupex').read()
    inno_cmd = inno_cmd.strip('\n')

inno_full_cmd = "%s --defaults-file=%s --port=%s --user=%s --password=%s %s "%(inno_cmd, conf_file, port, bak_user, bak_pwd, TODAYBACKUPPATH)
print inno_full_cmd
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
backup_start_time = datetime.datetime.now()
if os.system('%s;tar -zcvf %s.tar.gz %s;ls'%(inno_full_cmd,TODAYBACKUPPATH,TODAYBACKUPPATH)) == 0:
    print "mysql backup success."
else:
    print "mysql backup fail."
backup_finish_time = datetime.datetime.now()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
backup_total_time = (backup_finish_time - backup_start_time).total_seconds()/60
print  "the backup need %s minute."%(backup_total_time)

os.system('md5sum %s.tar.gz > %s.before.md5'%(TODAYBACKUPPATH,TODAYBACKUPPATH))
os.system('scp %s.* 192.168.56.142:/tmp'%(TODAYBACKUPPATH))
os.system('ssh 192.168.56.142;cmd /tmp/')
os.system('md5sum %s.tar.gz > %s.after.md5'%(TODAYBACKUPPATH,TODAYBACKUPPATH))

import filecmp
if filecmp.cmp(r'%s.before.md5'%(TODAYBACKUPPATH),r'%s.after.md5'%(TODAYBACKUPPATH)):
    print 'the data checksum finish,the is consistent.'
else:
    print 'Data has been damaged'



# innobackupex --defaults-file=/etc/my.cnf --port=3316 --user=root --password=123456 --stream=tar  /data/backup | gzip > /data/backup/`date +%F_%H-%M-%S`.tar.gz
#
# step 2:
# innobackupex --user=root --apply-log /data/2016-07-15_16-43-33
# step
# innobackupex --defaults-file=/data/3307/3307.cnf --user=root --copy-back /data/2016-07-15_16-43-33
#
#
# 压缩备份：
# innobackupex --defaults-file=/etc/my.cnf --port=3306 --databases="db_devon information_schema performance_schema mysql"  --user=inno_bak --password=123123 --stream=tar  /data/backup| gzip > /data/backup/`date +%F_%H-%M-%S`.tar.gz
# 非压缩备份：
# innobackupex --defaults-file=/etc/my.cnf --port=3306 --databases="db_devon information_schema performance_schema mysql"  --user=inno_bak --password=123123  /data/backup
#
# 恢复刚刚备份的备份数据库：
# step 1:
# innobackupex --user=root --apply-log /data/2016-11-06_21-14-37
# step 2:
# innobackupex --defaults-file=/etc/my.cnf --user=root --copy-back /data/2016-11-06_21-14-37
#
#
# innobackupex --user=root --apply-log opt/dbbackup/backup/physical/20180321/base_20180321
# innobackupex --defaults-file=/etc/my.cnf --user=root --copy-back opt/dbbackup/backup/physical/20180321/base_20180321

# tar备份和xbstream备份

# 判断备份软件是否安装

# 判断备份目录是否存在
# 检查数据库的状态
# 备份开始时间

#备份结束时间
#备份所需总时间
# 备份一致性校验
# 备份恢复情况
# 备份失败处理
# 备份过程中的日志记录

# innodbbackup备份时是否加入压缩合适。
# 远程连接到需要恢复的机器上，并确认是否连接确定机器，然后执行恢复操作。
# Getting current datetime to create seprate backup folder like "12012013-071334".

'''
# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print "checking for databases names file."
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print "Databases file found..."
    print "Starting backup of all dbs listed in file " + DB_NAME
else:
    print "Databases file not found..."
    print "Starting backup of database " + DB_NAME
    multi = 0

# Starting actual database backup process.
if multi:
   in_file = open(DB_NAME,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")

   while p <= flength:
       db = dbfile.readline()   # reading database name from file
       db = db[:-1]         # deletes extra line
       dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
       os.system(dumpcmd)
       compcmd = "tar -zcvf " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".tar.gz " +  pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
       os.system(compcmd)
       delcmd = "rm " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
       os.system(delcmd)
       p = p + 1
   dbfile.close()
else:
   db = DB_NAME
   dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
   os.system(dumpcmd)
   compcmd = "tar -zcvf " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".tar.gz " +  pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
   os.system(compcmd)
   delcmd = "rm " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
   os.system(delcmd)

print "Backup script completed"
print "Your backups has been created in '" + TODAYBACKUPPATH + "' directory"



'''
