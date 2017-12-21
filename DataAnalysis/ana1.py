#!/usr/bin/env python3
# _*_ coding: utf8 _*_

import pandas as pd
import numpy as np


# Reading data locally
df = pd.read_csv('/Users/devon/Documents/Test_File/pandas_test_file.csv')
df.head()

# Reading data from web
# data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
# df = pd.read_csv(data_url)

print(df['Complaint ID'].head())
print(df.dtypes)
print(df.sort_values('Complaint ID').head())


print(df.ix[:,0].head()) #打印第一列的前5行
