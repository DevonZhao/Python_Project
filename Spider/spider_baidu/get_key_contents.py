#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : get_key_contents.py
# @Author  : devon
# @Date    : 2018/2/3
# @Platform: Mac
# @version :
# @Desc    : 


#!/usr/bin/env python
# -*- coding=utf-8 -*-

import urllib3
import csv
import re
import os
import time
import requests
from bs4 import BeautifulSoup
import json
from write_mongo import conn_mongo
import pymongo

class FindRecord(object):
    def find_record(self,*key_word):
        headers = {
            'Cookie': 'userProvinceId=2; userCityId=0; userLocationId=26; proIp=123; ip_ck=4cKD5vP/j7QuNjUyMTk4LjE0Njk0Mzg5MzQ%3D; lv=1469438963; vn=1; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1469438964; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1469438964; z_day=rdetail=1; z_pro_city=s_provice%3Dshanghai%26s_city%3Dxingqu',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        }
        #请在这里修改想输入的关键词，如：京东，易到，搞笑,医疗卫生，郭德纲,共享单车,医院,大事件，医疗
        # key_word=('廊坊房价')
        for kw1 in key_word:
            for k in range(1,77):
                url = 'http://www.baidu.com/s?wd=%s&pn=%d&oq=%s&tn=monline_3_dg&ie=utf-8&usm=3'%(kw1 ,(k- 1)* 10,kw1)
                print(url)
                with open('dump_info_file.csv','w+') as csvfile:
                    # #wb写 a+追加模式
                    writer = csv.writer(csvfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    content = requests.get(url,headers).text #获取网页的html文本
                    #使用BeautifulSoup解析html
                    soup = BeautifulSoup(content,'lxml')
                for i in range(1,20):
                    try:

                        # contents0 = soup.find_all('div', {'class', 'c-span18 c-span-last'})[0]
                        # # print(contents)
                        # a01 = contents0.find(name="div", attrs={"class": re.compile("c-abstract")}).get_text()
                        # a02 = contents0.find(name="div", attrs={"data-tools": re.compile("title")})["data-tools"]
                        contents = soup.find_all('div',{'class', re.compile("result c-container")})[i]   # result c-container  c-span18 c-span-last
                        # print(contents)
                        a1 = contents.find(name="div", attrs={"class": re.compile("c-abstract")}).get_text()

                        a2 = contents.find(name="div", attrs={"data-tools": re.compile("title")})["data-tools"]
                        print(type(a1),type(a2))
                        print(a1)
                        print(a2)
                        # if a01 == a1 or a02 == a2:
                        #     print("progrem have been exited")
                        #     break
                        # else:
                        #

                        # if a1:
                        #     print(a1)
                        if a2:
                            # print(a2)
                            # print(json.loads(a2)['title'])
                            a2_tittle = json.loads(a2)['title']
                            # print(json.loads(a2)['url'])
                            a2_url = json.loads(a2)['url']
                            server_ip = "192.168.56.142"
                            port = 27017
                            mc = pymongo.MongoClient(server_ip, port)
                            dbname = mc.spiderdb
                            col = dbname.key_list
                            col.insert({"title": a2_tittle, "url": a2_url, "content": a1, "keyword":kw1})
                            # conn_mongo.col.insert({"tittle": a2_tittle, "url": a2_url, "content": a1})

                    except Exception as e:
                        # print(Exception,":",e)
                        pass
        return a1,a2_tittle,a2_url


if __name__ == '__main__':
    FindRecord().find_record('Python')