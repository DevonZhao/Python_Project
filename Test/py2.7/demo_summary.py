#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo_summary.py
# Description      :
# Author         :Devon
# Date          :2018/6/1
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

import MySQLdb
import sys,os

# 脚本来源网站：https://www.jb51.net/list/list_97_1.htm


def get_data(sql):
    db = MySQLdb.connect("10.9.2.72", "test_kill_user", "123123")
    cursor = db.cursor()
    cursor.execute(sql)
    d = cursor.fetchall()
    print d[0]
    print len(d)

    for row in xrange(len(d)):
        id = d[row][0]
        user = d[row][1]
        cmd = d[row][4]
        time = d[row][5]
        state = d[row][6]
        # print type(cmd),cmd

        try:
            if cmd.index('Sleep') > -1 and time > 100:
                if user.index('baymax_php') > -1:
                    print id,user,time,cmd,state
                    db1 = MySQLdb.connect("10.9.2.72", "test_kill_user", "123123")
                    cursor1 = db1.cursor()
                    kill_sql = 'kill %d;'%(id)
                    print kill_sql
                    cursor.execute(kill_sql)
                    db1.close()
        except Exception,o:
            pass
    print type(d)
    print d
    db.close()
    return d


def test_sql_data(sql):
    db = MySQLdb.connect("10.9.2.72", "test_kill_user", "123123")
    with db:
        cursor = db.cursor()
        cursor.execute(sql)
        d = cursor.fetchall()
        return d


#遍历字典
def traversal_dict():
    a = {'a': '1', 'b': '2', 'c': '3'}
    for key in a:
        print key + " :"+a[key]


# 获取当前时间对应unix时间戳
import datetime
import time
class GetNowTimestamp(object):
    def get_now_timestamp(self):
        return time.mktime(datetime.datetime.now().timetuple())

def common_code_seg():
    # 使用集合去除重复的元素
    targetList = [1,1,2,22,2,2,2,12]
    targetList = list(set(targetList))
    print targetList


def main():
    # get_data('show full processlist;')
    test_sql_data('show full processlist;')


if __name__ == '__main__':
    # main()
    # traversal_dict()
    # a1 = GetNowTimestamp()
    # print a1.get_now_timestamp()
    common_code_seg()





