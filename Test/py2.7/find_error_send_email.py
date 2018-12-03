#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :find_error_send_email.py
# Description      :
# Author         :Devon
# Date          :2018/12/3
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py
# python_version     :2.7.14
#==============================================================================

import re
import os
import time
import smtplib
import socket
import fcntl
import struct
from email.mime.text import MIMEText
from email.header import Header

class SendMail():
    def __init__(self):
        mail_host=''
        mail_user=''
        mail_pwd=''

    def send_mail(self, subject, msg, fromemail, pwd, email_lst):
        _user = fromemail
        _pwd = pwd
        _to = email_lst
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = MIMEText(msg, format, 'utf-8')
        msg["Subject"] = Header(subject, 'utf-8').encode()
        msg["From"] = _user
        msg["To"] = ",".join(_to)
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        try:
            s = smtplib.SMTP_SSL('smtp.126.com', 465)
            s.login(_user, _pwd)
            s.sendmail(_user, _to, msg.as_string())
            s.quit()
            print "[%s]INFO:Email send Success!" % nowtime
        except smtplib.SMTPException, e:
            print "[%s]ERROR:Email send Falied,%s" % (nowtime, e)

    def get_ip(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])


class ParseLog():
    def parse_log(self, pattern, error_log):
        re.compile(pattern)
        posfile = "/tmp/posfile"
        if not os.path.exists(posfile):
            os.mknod(posfile)
        if not os.path.getsize(posfile):
            with open(posfile, 'w') as fobj:
                fobj.write('0')
        f = open(error_log, 'r')
        f.seek(0, 2)
        endpos = f.tell()
        with open(posfile, 'r') as fobj:
            startpos = int(fobj.read())
            f.seek(startpos)

        if endpos - startpos > 0:
            data = f.read(endpos - startpos)  # 读取这么多个字节数
            f.close()
            with open(posfile, 'w') as fobj:
                fobj.write(str(endpos))
            m = re.findall(pattern, data, re.IGNORECASE)
            if m:
                content = '\n'.join(m)
                return content
            else:
                return ''

if __name__ == '__main__':
    sm = SendMail()  # 类的实例化
    pl = ParseLog()
    local_ip = sm.get_ip('eth0')
    subject = '服务器[%s]日志报警了！请处理！' % local_ip
    fromemail = '@126.com'
    pwd = ''
    email_lst = ['@7lk.com', '@qq.com']
    error_log = "/var/lib/mysql/bigdata.err"
    pattern = ".*Warning.*\s|.*error.*\s"
    while True:
        content = pl.parse_log(pattern, error_log)
        if content:
            sm.send_mail(subject, content, fromemail, pwd, email_lst)
