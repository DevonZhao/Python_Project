#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180118.py
# Description      :
# Author         :Devon
# Date          :2018/1/18
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

import shutil
import os
import sys
import logging

def record_log():
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    logger = logging.getLogger('test')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    # logger.debug('this is debug info')
    return logger

logger = record_log()

# 查看当前目录
print os.system('pwd')
print os.getcwd()

# 修改目录
os.chdir('..')
print os.getcwd()
print os.curdir
# os.path.getsize('demo180104.py')

a = os.path.isfile('demo180104.py')  # 判断是不是文件
print a
print os.listdir('Test')

# 关于目录的操作都在os.path下面。
print os.path.isdir('Test')

file_path = 'devon'
create_dir = 'devon'
if os.path.exists(file_path):
    print "这个目录已经存在，将被删除。"
    path_header = os.getcwd()  # 获取文件所在目录
    shutil.rmtree(file_path)  # 删除一个非空的目录，如果是空目录，则使用os.rmdir('devon')
    print "被删除的目录为%s/%s"%(path_header,file_path)
    logger.debug('记录错误日志。')

if os.path.isdir('Test'):
    os.mkdir(create_dir)
    os.chdir(create_dir) # 切换目录
    os.system('touch testfile.txt')
    os.mknod("test.txt")  # 创建一个空文件
    with open('test.txt', 'a+') as f:
        f.write('this is testing contents.')
    os.remove('testfile.txt')   # 删除一个文件
print os.getcwd()
print os.listdir('..')

