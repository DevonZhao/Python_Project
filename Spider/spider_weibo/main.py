#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : main.py
# @Author  : devon
# @Date    : 2018/2/8
# @Platform: Mac
# @version :
# @Desc    : 

import requests
from bs4 import BeautifulSoup
import re

def parse_contents():
    url = 'https://weibo.com/1712570933/G1SP7e6es?ref=feedsdk&type=comment#_rnd1517975034357'
    headers = {
                'Cookie': 'userProvinceId=2; userCityId=0; userLocationId=26; proIp=123; ip_ck=4cKD5vP/j7QuNjUyMTk4LjE0Njk0Mzg5MzQ%3D; lv=1469438963; vn=1; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1469438964; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1469438964; z_day=rdetail=1; z_pro_city=s_provice%3Dshanghai%26s_city%3Dxingqu',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
            }
    content = requests.get(url, headers).text
    st_code = requests.get(url, headers).status_code
    print(st_code)
    print(content)
    # try:
    #             r=requests.get(url,proxies=prox,headers=header)
    #             if r.status_code!=200:
    #                 continue
    #             else:
    #                 print "使用{0}连接成功>>".format(prox)
    #                 return r.content
    #         except Exception, e:
    #             return None

    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    # print(content)
    # print(soup)
    if st_code:
        c = soup.find_all(name="div")
        # print(c)

