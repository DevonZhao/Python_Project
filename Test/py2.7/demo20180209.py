#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180209.py
# Description      :
# Author         :Devon
# Date          :2018/2/9
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py
# 爬取搜房网信息数据
# 目的实现：分析哪些楼盘火热，什么时间买房火热，哪些开发商不错，哪些物业不错。买房的年龄和人群，房价的增长趋势图。
# 基本信息：房价，区域价格。

# python_version     :2.7.14
#==============================================================================

import sys
import requests
import re
from bs4 import BeautifulSoup
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

url1 = 'http://newhouse.fang.com/house/s/?from=pd'
url = 'http://bj.sofang.com/new/area'


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}



html = requests.get(url, headers=header)

def deal_code():
    print html.encoding
    print(html.headers['content-type'])
    print(html.apparent_encoding)
    print(requests.utils.get_encodings_from_content(html.text))

    if html.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(html.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = html.apparent_encoding
    return encoding

# enco = deal_code()
# encode_content = html.content.decode(enco, 'replace').encode('utf-8', 'replace')  # 这里只使用解码也是可以的。
# print encode_content
encode_content = html.content

soup = BeautifulSoup(encode_content,'lxml')
i = soup.find_all("a", target="_blank")
info_soup = soup.prettify()
print info_soup
# print i



