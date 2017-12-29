#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :test4.py
# Description      :I am test script
# Author         :Devon
# Date          :20160902
# Version        :0.1
# Usage         :python test4.py
# Notes         :
# python_version     :2.7.14
# 进一步完善：封装成一个类，然后对输出邮件的内容进行格式化。
# ==============================================================================

import os, sys
import smtplib

from subprocess import Popen, PIPE
from email.header import Header
from email.mime.text import MIMEText
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')
# 如果是多个邮件则使用逗号分开
to_list = ['@.com']
server_host = '..com'
username = '@.com'
password = ''


def get_data():
    db = MySQLdb.connect("192.168..", "", "")
    cursor = db.cursor()
    # cursor.execute("show all slaves status;")
    cursor.execute("show all slaves status;")
    d = cursor.fetchall()
    db.close()
    return d


def send_mail(to_list, sub, content):
    me = "manager" + "<" + username + ">"
    msg = MIMEText(content, _subtype='html')
    msg['Subject'] = Header(sub, 'utf-8').encode()
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(server_host)
        server.login(username, password)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
    except Exception as e:
        print str(e)


def parse_data():
    d = get_data()
    for i in range(len(d)):
        # print "Connection_name: "+d[i][0]
        # print "master server ip: "+d[i][3]
        # print "Slave_IO_Running: " + d[i][12]
        # print "Slave_SQL_Running: " + d[i][13]
        # print "Seconds_Behind_Master: " + str(d[i][34])
        mail_content = 'The following nodes have been down:    \n node name is:' + d[i][0] + '     \n master ip is:' + \
                       d[i][3] + '     \n Slave_IO_Running status is:' + d[i][
                           12] + '     \n Slave_SQL_Running status is:' + d[i][13]
        if d[i][12] == "Yes" and d[i][13] == "Yes":
            print 1
        else:
            print 0
            send_mail(to_list, 'BigData Mysql slave status:', mail_content)


if __name__ == '__main__':
    parse_data()


