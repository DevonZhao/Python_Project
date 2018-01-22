#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :del_binlog.py
# Description      :
# Author         :Devon
# Date          :2018/1/19
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

import os
from os.path import splitext
os.chdir('/tmp')
binlog_list = os.listdir('.')
lst = []
binlog_pre = 'binlog.00'
for i in binlog_list:
    # print os.path.splitext(i)[0]
    if splitext(i)[0] == 'binlog' and i <> 'binlog.index':
        lst.append(i[-4:])
for j in range(int(min(lst)),int(max(lst)) - 2):
    bin = binlog_pre+str(j)
    os.remove(bin)









