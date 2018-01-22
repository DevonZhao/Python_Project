#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180117.py
# Description      :
# Author         :Devon
# Date          :2018/1/17
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================


import logging
import sys,os

'''
处理流程：
    1.设置名
    2.设置格式，设置日志类型（文件或控制台）
    3.把2赋予1 ，设置日志级别（info，debug，warning），输出不同级别log，移除日志处理器。

常用方法：
    getLogger()
    Formatter()
    setFormatter()
    setLevel()
    FileHandler()
    StreamHandler()
    addHandler()
    removeHandler()

'''


logging.getLogger() # 这个是最基本入口
import logging
import sys

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("AppName")

# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# 文件日志
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)

# 输出不同级别的log
logger.debug('this is debug info')
logger.info('this is information')
logger.warn('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')

# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message

# 移除一些日志处理器
logger.removeHandler(file_handler)

# 记录log可以定义一个get_logger函数，然后调用这个函数，记录日志，还可以使用装饰器。

def get_logger():
    fmt = '%(levelname)s:%(message)s'
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(fmt))
    logger = logging.getLogger('App')
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    return logger


def call_me():
    logger = get_logger()
    logger.info('hi')


call_me()
