#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :soar.py
# Description      :
# Author         :Devon
# Date          :2018/11/1
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================
from os import environ

soar_configs = {
    'execuable_path': environ.get('soar', 'soar'),
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'blog',
    'skills': {
    	"-report-type":{
    		"type" : 1,
    		"default" : "text"
    	},
        "-allow-online-as-test":{
            "type" : 1,
            "default": "true"
        },
        "-profiling":{
            "type" : 1,
            "default": "true"
        },
        # "-trace":{
        #     "type" : 1,
        #     "default": "true"
        # },
        "-verbose":{
            "type" : 1,
            "default": "true"
        }
    }
}

from subprocess import Popen, PIPE
import pymysql.cursors
from shlex import split

def execute_commond_get_stdout(commond):
    commond_list = split(commond)
    p = Popen(commond_list, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    print({'code':p.returncode, 'stdout':stdout, 'stderr':stderr})
    if p.returncode !=0:
        return stderr.decode(errors='ignore')
    elif len(stderr) != 0:
        return stderr.decode(errors='ignore')
    return stdout.decode(errors='ignore')

def get_databases(host, port, user, password):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 port=port,
                                 db='information_schema')
    databases = list()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT schema_name FROM information_schema.schemata'
            cursor.execute(sql)
            result = cursor.fetchall()
            for result_tuple in result:
                databases.append(result_tuple[0])
    except Exception as e:
        raise Exception('查询数据库失败，失败原因:%s' % str(e))
    else:
        return databases
    finally:
        connection.close()

class SOAR:
    def execute_sql_analysis(self, choosed_plugins, args):
        result = dict()
        for plugin_name in choosed_plugins:
            plugin_instance = getattr(self, plugin_name, None)
            if plugin_instance is None:
                raise TypeError('unsupported plugin')
            commond = plugin_instance.generate_query_commond(args)
            try:
                stdout = plugin_instance.execute_commond(commond)
            except Exception as e:
                stdout = '执行命令出错：%s' % str(e)
            result[plugin_name] = stdout
        return result


class Soar(Plugin):

    def __init__(self, configs):
        self.read_config(configs)

    def _generate_conn_str(self, args):
        return '{}:{}@{}:{}/{}'.format(args.get('user', self._configs.get('user')),
                                       args.get('password', self._configs.get('password')),
                                       args.get('host', self._configs.get('host')),
                                       args.get('port', self._configs.get('port')),
                                       args.get('database', self._configs.get('database')))

    def generate_query_commond(self, args):
        command_str = self._configs['execuable_path'] + ' '
        for skill_name, skill_content_dict in self._configs['skills'].items():
            if skill_content_dict['type'] == 0:
                command_str += ' {} '.format(skill_name)
            if skill_content_dict['type'] == 1:
                command_str += ' {}={} '.format(skill_name, skill_content_dict['default'])
        conn_str = self._generate_conn_str(args)
        command_str += ' -test-dsn="{}" '.format(conn_str)
        command_str += ' -query="{}" '.format(args.get('sql'))
        return command_str

    def execute_commond(self, commond):
        print(commond)
        return execute_commond_get_stdout(commond)