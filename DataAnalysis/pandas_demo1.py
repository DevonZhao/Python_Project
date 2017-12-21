#! /usr/lib/pandas3/bin/env python
# -*- coding: utf-8 -*-
# Title         :test4.py
# Description      :I am test script
# Author         :Devon
# Date          :20160902
# Version        :0.1
# Usage         :python test4.py
# Notes         :
# python_version     :2.7.14
#==============================================================================

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

s = pd.Series([1, 2, 3, np.nan , 44, 1])
print(s)
dates = pd.date_range('20170101',periods=6)
print(dates)

obj = pd.Series(np.arange(5.),index=['a','b','c','d','e'])
new_obj = obj.drop('c')
print(obj)
print(obj['b':'c'])
print(obj[1:2])

data = pd.DataFrame(np.arange(16).reshape((4,4)),index =['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'] )

print(data)

print(data[['three', 'one']])