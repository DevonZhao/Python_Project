#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :add_slave_to_new_master.py
# Description      :
# Author         :Devon
# Date          :2018/6/22
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py
# python_version     :2.7.14
#==============================================================================

import os,sys
import MySQLdb

def get_change_master_statement():
    lst_i =[]
    manger_log = '/root/manager.log'
    find_str = 'CHANGE MASTER TO'
    with open(manger_log) as f:
        lst = f.readlines()
    for i in xrange(len(lst)):
        if (lst[i].find(find_str) != -1):   # 找出特定字符串
            lst_i.append(i)
    npos = lst[max(lst_i)].index('CHANGE MASTER TO')
    change_master_statement = lst[max(lst_i)][npos:]
    return change_master_statement

# 执行sql语句函数
def exec_change_master(sql,ip,user,pwd):
    db = MySQLdb.connect(ip, user, pwd)
    try:
        with db:
            cursor = db.cursor()
            cursor.execute(sql)
            d = cursor.fetchall()
            return d
    except Exception,e:
        print "Error:",Exception,",",e


# 判断mysql是否运行，没有运行则需要启动。可以手动启动。

def main():
    repl_pwd = '123456'
    ip = '192.168.56.151'
    user = 'dbadmin'
    pwd = '123123'
    sql = get_change_master_statement()
    print sql.replace("xxx';", "%s';start slave;")%(repl_pwd)
    new_sql = sql.replace("xxx';", "%s';start slave;")%(repl_pwd)
    print exec_change_master(new_sql,ip,user,pwd)
    print get_change_master_statement()  # return需要打印print

if __name__ == '__main__':
    main()



