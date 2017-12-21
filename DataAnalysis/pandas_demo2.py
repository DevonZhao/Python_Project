#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :test4.py
# Description      :I am test script
# Author         :Devon
# Date          :20160902
# Version        :0.1
# Usage         :python test4.py
# Notes         :
# python_version     :3.6
#==============================================================================

import pandas as pd
import numpy as np
import xlrd

import sys
# read excel file and print it , and then reversal print df.

excel_file = r"/pyapp/file/cdn_header.xlsx"
df = pd.read_excel(excel_file)

pd.concat()
print(df)
print(type(df))

print(sys.argv)  # 获取传入参数列表，如果不传入任何参数则只有argv[0]表示代码本身文件路径