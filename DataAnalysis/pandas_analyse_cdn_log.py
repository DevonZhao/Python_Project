#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :test4.py
# Description   :根据CDN日志过滤一些数据，例如流量、状态码统计，TOP IP、URL、UA、Referer等
# Author         :Devon
# Date          :20160902
# Version        :0.1
# Usage         :python test4.py
# Notes         :
# python_version     :3
#==============================================================================
import pandas as pd
import numpy as np
import sys
from collections import OrderedDict

# if len(sys.argv) != 2:
#     print('Usage:',sys.argv[0],'file_of_log')
#     exit()
# else:
#     log_file = sys.argv[1]

# 需统计字段对应的日志位置
ip = 1
url = 3
status_code = 7
size = 4
referer = 8
ua = 10

log_file = r"/pyapp/file/cdn.txt"

# 将日志读入DataFrame
reader = pd.read_table(log_file, sep=' ', names=[i for i in range(16)], iterator=True)

loop = True
chunkSize = 10000000
chunks = []
while loop:
    try:
        chunk = reader.get_chunk(chunkSize)
        chunks.append(chunk)
        # print(chunks)
    except StopIteration:
        #Iteration is stopped.
        loop = False
df = pd.concat(chunks, ignore_index=True)
print(df[size])
byte_sum = df[size].sum()        #流量统计
top_status_code = pd.DataFrame(df[6].value_counts())      #状态码统计
top_ip  = df[ip].value_counts().head(10)      #TOP IP
top_referer = df[referer].value_counts().head(10)      #TOP Referer
top_ua  = df[ua].value_counts().head(10)      #TOP User-Agent
top_status_code['persent'] = pd.DataFrame(top_status_code/top_status_code.sum()*100)
top_url  = df[url].value_counts().head(10)      #TOP URL
top_url_byte = df[[url,size]].groupby(url).sum().apply(lambda x:x.astype(float)/1024/1024) \
   .round(decimals = 3).sort_values(by=[size], ascending=False)[size].head(10) #请求流量最大的URL
top_ip_byte = df[[ip,size]].groupby(ip).sum().apply(lambda x:x.astype(float)/1024/1024) \
   .round(decimals = 3).sort_values(by=[size], ascending=False)[size].head(10) #请求流量最多的IP
# 将结果有序存入字典
result = OrderedDict([("流量总计[单位:GB]:"   , byte_sum/1024/1024/1024),
   ("状态码统计[次数|百分比]:"  , top_status_code),
   ("IP TOP 10:"    , top_ip),
   ("Referer TOP 10:"   , top_referer),
   ("UA TOP 10:"    , top_ua),
   ("URL TOP 10:"   , top_url),
   ("请求流量最大的URL TOP 10[单位:MB]:" , top_url_byte),
   ("请求流量最大的IP TOP 10[单位:MB]:" , top_ip_byte)
])
# 输出结果
for k,v in result.items():
 print(k)
 print(v)
 print('='*80)

