#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :mysql_to_excel.py
# Description      :
# Author         :Devon
# Date          :2018/1/30
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================
# 如何让一个包可以使用pip安装
# xlwt对写入excel的行数有限制65536，可以使用openpyxl代替。


# 修复bug，在sql中包含列的别名为中文报错:UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)
#         这个错误是因为write方法接收的是unicode编码的字符串，改变编码即可，python3估计不会有这个问题，不过没有进行测试。

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xlwt
import MySQLdb
from argparse import ArgumentParser, RawTextHelpFormatter


import chardet

class Mysql2Excel(object):
    # ----------
    # get_args()函数通过argparse模块的ArgumentParser类来生成帮助信息并获取命令行参数
    # 生成一个全局变量字典对象args，保存处理过的命令行参数
    # ----------
    def get_args(self):
        # 实例化类，formatter_class参数允许help信息以自定义的格式显示
        parser = ArgumentParser(
            description="\n\nThis is a simple tool for MySQL DBA or RD.\n"
                        "With this tool you can automatically and quickly export the data you need.\n"
                        "You can find help information by using -h or --help.",
            formatter_class=RawTextHelpFormatter)
        parser.add_argument('-H', metavar='HOSTNAME', dest='host', help="mysql hostname", required=True)
        parser.add_argument('-u', metavar='USER', dest='user', help="mysql user", required=True)
        parser.add_argument('-p', metavar='PASSWORD', dest='password', help="mysql password", required=True)
        parser.add_argument('-d', metavar='DATABASE', dest='dbname', help="mysql database name", required=True)
        parser.add_argument('-t', metavar='TABLE', dest='table_name', help="mysql table name", required=True)
        parser.add_argument('-s', metavar='SQL', dest='sql', help="sql statement", required=True, )
        parser.add_argument('-o', metavar='PATH', dest='outputpath', help="export path", )
        parser.add_argument('-P', metavar='PORT', dest='port', help="mysql port(default 3306)", default=3306, type=int,  )
        global args
        args = vars(parser.parse_args())
        # print(args)

    # table_name和sql只能有一个为空
    def export_data(self,host,user,password,dbname,table_name,sql,outputpath):
        conn = MySQLdb.connect(host,user,password,dbname,charset='utf8')
        cursor = conn.cursor()
        if sql.strip():
            count = cursor.execute(sql)
        else:
            count = cursor.execute('select * from ' + table_name)
        # 重置游标的位置
        cursor.scroll(0, mode='absolute')
        results = cursor.fetchall()
        fields = cursor.description
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('table_'+table_name,cell_overwrite_ok=True)
        for field in range(0,len(fields)):
            a = fields[field][0]
            b = u''+ fields[field][0]   # write方法接收的是unicode类型的字符串。
            sheet.write(0,field,b)
        row = 1
        col = 0
        for row in range(1,len(results)+1):
            for col in range(0,len(fields)):
                print results[row-1][col]
                sheet.write(row,col,u'%s'%results[row-1][col])
        workbook.save(outputpath)

if __name__ == "__main__":
    mysql = Mysql2Excel()
    mysql.get_args()
    mysql.export_data(args['host'], args['user'], args['password'], args['dbname'], args['table_name'], args['sql'], r''+ args['outputpath'])    # 【r''+ 变量名】表示是原始字符





#
# # ----------
# # process_query()函数从get_args()返回值中拿到登陆mysql需要的相关信息
# # 执行show global status语句，并将结果保存在status_dict字典中
# # ----------
# def process_query():
#     status_dict = {}  # 存放所有status值
#     try:
#         with pymysql.connect(host=args['host'], user=args['user'], password=args['password'], charset='utf8',
#                              port=args['port']) as mysql_cur:
#             mysql_cur.execute('show global status')  # 执行语句，查询结果的每一行作为一个元组存进mysql_cur中
#     except pymysql.err.MySQLError as err:
#         print("ERROR: " + str(err))
#         exit(10)
#
#     for status in mysql_cur:
#         status_dict[status[0]] = status[1]  # 更新status_dict字典
#     return status_dict
#
#
# # ----------
# # show_result()函数处理相关数据，展示最终结果
# # ----------
# def show_result(type):
#     # 打印头部
#     print()
#     for status in types_dic[args['type']]:
#         print('     {}'.format(status), end='')
#         print()
#
#         # 开始循环显示
#         try:
#             while True:
#                 status_dic1 = process_query()
#                 sleep(args['interval'])
#                 status_dic2 = process_query()
#                 # 打印各值
#                 for k in types_dic[args['type']]:
#                     if args['average'] is True:
#                         # 有--average选项，输出指定时间内的平均值
#                         print(
#                         '     ' + str(round((int(status_dic2[k]) - int(status_dic1[k])) / args['interval'], 2)).center(
#                             len(k)), end='' )
#                         else:
#                         # 输出指定时间内的增长值
#                         print('     ' + str(round(int(status_dic2[k]) - int(status_dic1[k]))).center(len(k)), end='' )
#                         print()
#                 except KeyboardInterrupt:
#                 print('\n-----bye-----')
#
#         if __name__ == '__main__':
#             get_args()
#             process_query()
#             show_result(args['type'])