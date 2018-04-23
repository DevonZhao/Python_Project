#!/usr/bin/env python3
# _*_ coding: utf8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# Reading data locally
df = pd.read_csv('/Users/devon/Documents/Test_File/pandas_test_file.csv')
df.head()

# Reading data from web
# data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
# df = pd.read_csv(data_url)

print(df['Complaint ID'].head())
print(df.dtypes)
print(df.sort_values('Complaint ID').head())


print(df.ix[:,0].head())  # 打印第一列的前5行
print(df.ix[10:20, 0:3])  # 取出从11到20行的前3列数据
print("*"*100)

print(df.describe())  # 对数据的统计特性进行描述

print("*"*100)


