#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :mysql_binlog_stat.py
# Description      :
# Author         :Devon
# Date          :2018/9/18
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

# !/usr/bin/env python
# -*- coding:utf-8 -*-

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import UpdateRowsEvent
from pymysqlreplication.row_event import WriteRowsEvent
from pymysqlreplication.row_event import DeleteRowsEvent
from pymysqlreplication.event import XidEvent,BeginLoadQueryEvent,QueryEvent
import time
import argparse
import simplejson as json
import sys
import signal
import traceback



class MySQLBinlogStat(object):
    """对MySQL Binlog Event进行解析,获得对MySQL操作的统计"""

    _stream = None
    _table_stat_info = {}

    def __init__(self, stream):
        self.stream = stream

    @property
    def stream(self):
        """stream 是一个属性 - getter 方法"""
        return self._stream

    @stream.setter
    def stream(self, value):
        """stream属性的 setter 方法"""
        self._stream = value

    @property
    def table_stat_info(self):
        """table_stat_info 是一个属性 - getter 方法"""
        return self._table_stat_info

    @table_stat_info.setter
    def table_stat_info(self, value):
        """table_stat_info属性的 setter 方法"""
        self._table_stat_info = value

    def init_schema_stat_struct(self, schema=None):
        """初始化记录表统计信息的数据库基本结构
        Args:
            schema: 数据库名称
        Return: None
        Raise: None
        Table stat info struct:
            _table_stat_info = {
                'test': { # 数据库名称
                }
            }
        """
        # print type(self.table_stat_info)
        if schema not in self.table_stat_info:  # 初始化 数据库
            self.table_stat_info[schema] = {}

    def init_table_stat_struct(self, schema=None, table=None):
        """初始化记录表统计信息的表的基本结构
        Args:
            schema: 数据库名称
            table: 表名称
        Return: None
        Raise: None
        Table stat info struct:
            _table_stat_info['test'] = {
                't1': { # 表名称
                    'table_dml_count': { # 统计表 DML 次数的变量
                        'insert': 0,
                        'update': 0,
                        'delete': 0,
                    },
                    'row_insert_count': {}, # 统计表的字段插入数
                    'row_update_count': {}, # 统计表的字段更新数
                }
            }
        """

        if table not in self.table_stat_info[schema]:  # 初始化表
            self.table_stat_info[schema][table] = {
                'table_dml_count': {  # 统计表 DML 次数的变量
                    'insert': 0,
                    'update': 0,
                    'delete': 0,
                },
                'row_insert_count': {},  # 统计表的字段插入数
                'row_update_count': {},  # 统计表的字段更新数
            }

    def init_insert_col_stat_struct(self, schema=None, table=None, col=None):
        """初始化插入字段统计结构
        Args:
            schema: 数据库
            table: 表
            col: 字段
        Return: None
        Raise: None
        """

        self.table_stat_info[schema][table]['row_insert_count'][col] = 0

    def init_update_col_stat_struct(self, schema=None, table=None, col=None):
        """初始化更新字段统计结构
        Args:
            schema: 数据库
            table: 表
            col: 字段
        Return: None
        Raise: None
        """

        self.table_stat_info[schema][table]['row_update_count'][col] = 0

    def schema_exist(self, schema=None):
        """判断schema是否存在
        Args:
            schema: 数据库
        Return: True/False
        Raise: None
        """

        if schema in self.table_stat_info:
            return True
        else:
            return False

    def table_exist(self, schema=None, table=None):
        """判断表是否存在
        Args:
            schema: 数据库
            table: 表
        Return: True/False
        Raise: None
        """

        if table in self.table_stat_info[schema]:
            return True
        else:
            return False

    def insert_col_exist(self, schema=None, table=None, col=None):
        """判断插入的字段是否存在
        Args:
            schema: 数据库
            table: 表
            col: 字段名
        Return: True/False
        Raise: None
        """

        if col in self.table_stat_info[schema][table]['row_insert_count']:
            return True
        else:
            return False

    def update_col_exist(self, schema=None, table=None, col=None):
        """判断更新的字段是否存在
        Args:
            schema: 数据库
            table: 表
            col: 字段名
        Return: True/False
        Raise: None
        """

        if col in self.table_stat_info[schema][table]['row_update_count']:
            return True
        else:
            return False

    def add_insert_count(self, schema=None, table=None, count=0):
        """添加insert执行的行数
        Args:
            schema: 数据库
            table: 表
            count: 行数
        """

        self.table_stat_info[schema][table] \
            ['table_dml_count']['insert'] += count

    def add_update_count(self, schema=None, table=None, count=0):
        """添加update执行的行数
        Args:
            schema: 数据库
            table: 表
            count: 行数
        """

        self.table_stat_info[schema][table] \
            ['table_dml_count']['update'] += count

    def add_delete_count(self, schema=None, table=None, count=0):
        """添加delete执行的行数
        Args:
            schema: 数据库
            table: 表
            count: 行数
        """

        self.table_stat_info[schema][table] \
            ['table_dml_count']['delete'] += count

    def add_insert_row_col_count(self, schema=None, table=None,
                                 col=None, count=0):
        """添加insert语句列的插入次数
        Args:
            schema: 数据库
            table: 表
            col: 列名
            count: 更新新次数
        """

        self.table_stat_info[schema][table] \
            ['row_insert_count'][col] += count

    def add_update_row_col_count(self, schema=None, table=None,
                                 col=None, count=0):
        """添加insert语句列的插入次数
        Args:
            schema: 数据库
            table: 表
            col: 列名
            count: 更新新次数
        """

        self.table_stat_info[schema][table] \
            ['row_update_count'][col] += count

    def insert_row_stat(self, binlogevent=None):
        """对WriteRowsEvent事件进行分析统计
        Args:
            binlogevent: binlog 事件对象
        Return: None
        Raise: None
        """

        # 判断之前是否存在该表的统计信息, 不存在则初始化一个

        schema = binlogevent.schema
        table = binlogevent.table
        # print schema,table
        # print binlogevent.rows
        # print binlogevent.event_size
        if not self.schema_exist(schema=schema):  # 初始化 schema
            self.init_schema_stat_struct(schema=schema)

        if not self.table_exist(schema=schema, table=table):  # 初始化 table
            self.init_table_stat_struct(schema=schema, table=table)

        self.add_insert_count(schema=schema, table=table,
                              count=len(binlogevent.rows))  # 添加 INSERT 行数

    def dml_trx_stat(self, binlogevent=None):
        """对WriteRowsEvent事件进行分析统计
        Args:
            binlogevent: binlog 事件对象
        Return: None
        Raise: None
        """

        # 判断之前是否存在该表的统计信息, 不存在则初始化一个

        schema = binlogevent.schema
        table = binlogevent.table
        # print schema,table
        # print binlogevent.rows
        # print binlogevent.event_size
        if not self.schema_exist(schema=schema):  # 初始化 schema
            self.init_schema_stat_struct(schema=schema)

        if not self.table_exist(schema=schema, table=table):  # 初始化 table
            self.init_table_stat_struct(schema=schema, table=table)

        self.add_insert_count(schema=schema, table=table,
                              count=len(binlogevent.rows))  # 添加 INSERT 行数

    def update_row_stat(self, binlogevent=None):
        """对UpdateRowsEvent事件进行分析统计
        Args:
            binlogevent: binlog 事件对象
        Return: None
        Raise: None
        """

        # 判断之前是否存在该表的统计信息, 不存在则初始化一个
        schema = binlogevent.schema
        table = binlogevent.table

        if not self.schema_exist(schema=schema):  # 初始化 schema
            self.init_schema_stat_struct(schema=schema)

        if not self.table_exist(schema=schema, table=table):  # 初始化 table
            self.init_table_stat_struct(schema=schema, table=table)

        self.add_update_count(schema=schema, table=table,
                              count=len(binlogevent.rows))  # 添加 INSERT 行数

    def delete_row_stat(self, binlogevent=None):
        """对DeleteRowsEvent事件进行分析统计
        Args:
            binlogevent: binlog 事件对象
        Return: None
        Raise: None
        """

        # 判断之前是否存在该表的统计信息, 不存在则初始化一个
        schema = binlogevent.schema
        table = binlogevent.table

        if not self.schema_exist(schema=schema):  # 初始化 schema
            self.init_schema_stat_struct(schema=schema)

        if not self.table_exist(schema=schema, table=table):  # 初始化 table
            self.init_table_stat_struct(schema=schema, table=table)

        self.add_delete_count(schema=schema, table=table,
                              count=len(binlogevent.rows))  # 添加 DELETE 行数

    def insert_row_col_stat(self, binlogevent):
        """统计insert某列的值"""

        schema = binlogevent.schema
        table = binlogevent.table
        row_size = len(binlogevent.rows)

        for column in binlogevent.columns:
            # 初始化列的统计
            if not self.insert_col_exist(schema=schema, table=table,
                                         col=column.name):
                self.init_insert_col_stat_struct(schema=schema,
                                                 table=table,
                                                 col=column.name)
            self.add_insert_row_col_count(schema=schema, table=table,
                                          col=column.name, count=row_size)

    def update_row_col_stat(self, binlogevent):
        """统计update某列的值"""

        schema = binlogevent.schema
        table = binlogevent.table

        for row in binlogevent.rows:
            for column in binlogevent.columns:
                if column.is_primary:  # 是主键则不处理
                    continue

                # 前后的值相等则不处理
                if (row['before_values'][column.name] ==
                        row['after_values'][column.name]):
                    continue

                # 初始化更新列统计
                if not self.update_col_exist(schema=schema, table=table,
                                             col=column.name):
                    self.init_update_col_stat_struct(schema=schema,
                                                     table=table,
                                                     col=column.name)

                # 添加某列更行1次
                self.add_update_row_col_count(schema=schema, table=table,
                                              col=column.name, count=1)

    def run_parse(self):
        """循环解析并统计"""
        dict = {}
        d = {}
        lst = []
        for binlogevent in self.stream:
            # binlogevent._dump()

            if binlogevent.event_type in [23, 30]:  # WriteRowsEvent(WRITE_ROWS_EVENT)
                # print binlogevent.timestamp
                self.insert_row_stat(binlogevent)
                self.insert_row_col_stat(binlogevent)
            elif binlogevent.event_type in [24, 31]:  # UpdateRowsEvent(UPDATE_ROWS_EVENT)
                self.update_row_stat(binlogevent)
                self.update_row_col_stat(binlogevent)
            elif binlogevent.event_type in [25, 32]:  # DeleteRowsEvent(DELETE_ROWS_EVENT)
                self.delete_row_stat(binlogevent)
            elif binlogevent.event_type in [16]:
                # print binlogevent.event_type, binlogevent.xid, binlogevent.event_size, binlogevent.timestamp
                pass
            else:
                # print binlogevent.event_type,binlogevent.event_size,binlogevent.timestamp
                pass

            if binlogevent.event_type in [2]:  # begin
                begin_time = binlogevent.timestamp
                print "begin time:",begin_time

            if binlogevent.event_type in [23, 30, 24, 31, 25, 32]:
                if binlogevent.event_type in [23, 30]:
                    insert_count = len(binlogevent.rows)
                    dict['insert'] = insert_count

                if binlogevent.event_type in [24, 31]:
                    update_count = len(binlogevent.rows)
                    dict['update'] = update_count
                if binlogevent.event_type in [25, 32]:
                    delete_count = len(binlogevent.rows)
                    dict['delete'] = delete_count
                print dict
                lst.append(dict)


                    # for schema, tables in self.table_stat_info.iteritems():
                #     for table, stat in tables.iteritems():
                #         key = '{schema}.{table}'.format(schema=schema, table=table)
                #         print stat['table_dml_count']

            if binlogevent.event_type in [16]:  # xid,commit
                end_time = binlogevent.timestamp
                print "end time:",end_time
                print (end_time-begin_time),binlogevent.xid  #添加pos点
        print lst
            # {
            #     "xid:569": {
            #         "insert": 10,
            #         "update": 5,
            #         "delete": 0
            #     }
            # }




    # 打印出json格式
    def print_format(self, content):
        print json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=4)

    def print_sort_stat(self, by='insert'):
        """排序打印统计结果"""

        by = by.lower()  # 一律转化为小写

        # 对统计进行排序
        stat = self.iter_table_stat_format()
        sorted_stat = sorted(
            self.iter_table_stat_format(),
            key=lambda stat: stat.values()[0][by],
            reverse=True,
        )
        self.print_format(sorted_stat[0:6])  #排序后取前5个

    def iter_table_stat_format(self):
        """格式化每个表的统计的dict
        Format: {'schema.table': xxx}
        """
        for schema, tables in self.table_stat_info.iteritems():
            for table, stat in tables.iteritems():
                key = '{schema}.{table}'.format(schema=schema, table=table)
                # print {key: stat['table_dml_count']}
                # print {key: stat['table_dml_count']}.values()[0]['insert']
                yield {key: stat['table_dml_count']}


    def print_trx_dml_res(self):
        for schema, tables in self.table_stat_info.iteritems():
            for table, stat in tables.iteritems():
                key = '{schema}.{table}'.format(schema=schema, table=table)
                yield {key: stat['table_dml_count']}



def parse_args():
    """解析命令行传入参数"""
    usage = """
        Description:
            The script parse MySQL binlog and statistic column.
    """

    # 创建解析对象并传入描述
    parser = argparse.ArgumentParser(description=usage)
    # 添加 MySQL Host 参数
    parser.add_argument('--host', dest='host', action='store',
                        default='127.0.0.1', help='Connect MySQL host',
                        metavar='HOST')
    # 添加 MySQL Port 参数
    parser.add_argument('--port', dest='port', action='store',
                        default=3306, help='Connect MySQL port',
                        metavar='PORT', type=int)
    # 添加 MySQL username 参数
    parser.add_argument('--username', dest='username', action='store',
                        default='root', help='Connect MySQL username',
                        metavar='USERNAME')
    # 添加 MySQL password 参数
    parser.add_argument('--password', dest='password', action='store',
                        default='root', help='Connect MySQL password',
                        metavar='PASSWORD')
    # 添加 MySQL binlog file 参数
    parser.add_argument('--log-file', dest='log_file', action='store',
                        default=None, help='Specify a binlog name',
                        metavar='binlog-file-name')
    # 添加 MySQL binlog file pos 参数
    parser.add_argument('--log-pos', dest='log_pos', action='store',
                        default=None, help='Specify a binlog file pos',
                        metavar='binlog-file-pos', type=int)
    # 添加 slave server id 参数
    parser.add_argument('--server-id', dest='server_id', action='store',
                        default=99999, help='Specify a slave server server-id',
                        metavar='server-id', type=int)
    # 添加 slave uuid 参数
    parser.add_argument('--slave-uuid', dest='slave_uuid', action='store',
                        default='ca1e2b93-5d2f-11e6-b758-0800277643c8',
                        help='Specify a slave server uuid', metavar='slave-uuid')
    # 添加 是否以阻塞的方式进行解析 参数
    parser.add_argument('--blocking', dest='blocking', action='store',
                        default=False, help='Specify is bloking and parse, default False',
                        metavar='False/True')
    # 添加指定以什么时间戳开始进行解析
    help = 'Specify is start parse timestamp, default None, example: 2016-11-01 00:00:00'
    parser.add_argument('--start-time', dest='start_time', action='store',
                        default=None, help=help, metavar='start-time')
    # 添加 是否以阻塞的方式进行解析 参数
    parser.add_argument('--sorted-by', dest='sorted_by', action='store',
                        default='insert', help='Specify show statistic sort by, default: insert',
                        metavar='insert/update/delete')

    args = parser.parse_args()

    return args


def kill_sign_op(signum, frame):
    """当接收到kill 信号执行关闭流打印输出 和"""

    global mysql_binlog_stat  # 使用全局mysql_binlog_stat

    if mysql_binlog_stat != None:  # 不为空才执行

        # 关闭流
        mysql_binlog_stat.stream.close()

        # 打印数据
        mysql_binlog_stat.print_sort_stat()

    sys.exit(0)


# 定义全局变量
mysql_binlog_stat = None


def main():
    global mysql_binlog_stat  # 使用前面的全局变量

    # 注册 捕获型号kill信号
    signal.signal(signal.SIGTERM, kill_sign_op)

    args = parse_args()  # 解析传入参数

    mysql_settings = {
        'host': args.host,
        'port': args.port,
        'user': 'rt',
        'passwd': '123123',
    }

    skip_to_timestamp = (
        time.mktime(time.strptime(args.start_time, '%Y-%m-%d %H:%M:%S'))
        if args.start_time else None
    )

    stream_conf = {
        'connection_settings': mysql_settings,
        'server_id': args.server_id,
        'slave_uuid': args.slave_uuid,
        'blocking': args.blocking,
        'log_file': '/var/lib/mysql/binlog/binlog.000007',
        'log_pos': args.log_pos,
        'skip_to_timestamp': skip_to_timestamp,
        'only_events': [UpdateRowsEvent, WriteRowsEvent, DeleteRowsEvent,XidEvent,BeginLoadQueryEvent,QueryEvent],
    }
    # print stream_conf


    stream = BinLogStreamReader(**stream_conf)  #定义一个stream

    # for a1 in stream:
    #     print a1.dump()

    mysql_binlog_stat = MySQLBinlogStat(stream)
    try:
        mysql_binlog_stat.run_parse()

    except KeyboardInterrupt:  # 捕捉 KeyboardInterrupt 异常
        print 'force to exit...'

    except Exception as e:
        print traceback.format_exc()

    finally:  # 最终需要关闭流
        mysql_binlog_stat.stream.close()
    # 打印数据
    mysql_binlog_stat.print_sort_stat(by=args.sorted_by)

if __name__ == '__main__':
    main()