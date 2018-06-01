#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :maimai_word_activity_2017.py
# Description      :爬去脉脉数据
# Author         :Devon Zhao
# Date          :2018-01-02
# Version        :1.0
# Usage         :爬取脉脉网站的数据url地址为：https://maimai.cn/article/word_activity_2017?fr=feed_list   这个是统计脉脉上用户用一个字一句话描述自己的2017。
# python_version     :3.6
#遇到问题，这个网页是需要下来才能加载如下内容，这是爬虫的一类，好多网站都存在这样的问题。
# 使用那些知识：1.使用request.get获取内容 2.解析json 3.爬取下拉网页 4.等待几秒然后再爬 5.发爬机制 6.request用法
# 根据输入选项，选择保存的方式，比如说1保存为文件 2.保存到数据库，3.保存到mongo 4.保存为excel格式
# 如何解决ip被封杀问题
# 使用代理服务器
# 处理短时间爬太多不让爬的问题


from bs4 import BeautifulSoup
import os,sys
import re
import pandas as pd
import numpy as np
import requests
import urllib
import urllib3
import json
import time
import random

def get_part_data():
    url = 'https://maimai.cn/article/word_activity_2017?fr=feed_list'
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}
    html = requests.get(url, headers=header).content
    soup = BeautifulSoup(html,'lxml')
    contents = soup.select('.halfWidth ')

    i = 1
    try:
        for i in range(len(contents)):
            if len(contents[i].select('.ny_name')) < 1:
                continue
            else:
                print(contents[i].select('.ny_name')[0].get_text())
                print(contents[i].select('.ny_word')[0].get_text())
                print(contents[i].select('.ny_text_summary')[0].get_text())
                print(contents[i].select('.font-13')[0].get_text())
                print('*'*100)
    except IndexError:
        print("IndexError: list index out of range")




# def get_header():
#
#
#
#
# def get_data():
#
#

#
# file_name = open('maimai_word_activity.txt', "ab+")
# file_name.write(('\r' + file_name + '\r\n').encode('UTF-8'))
#
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0
# 3600

j = 0
def parse_json():
    j = 0
    while j < 3600:
        url = "https://maimai.cn/sdk/article/get_words?count=20&page=%d&uinfo=636366&wxtoken=&year=2017&fr=feed_list"%(j)
        user_agent = ['Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0','Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
                      'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                      'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36','Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19']
        ua = random.choice(user_agent)  # 在user-agent列表里随机去除一个作为当前header的user-agent
        print(ua)
        header = {'User-Agent': ua,
                 'Connection': 'keep-alive',
                  'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                  'Accept-Encoding': 'gzip, deflate'}
        r = requests.get(url, headers=header)
        print(r.status_code)

        try:
            share_data = r.content.decode('utf-8')  #  转化字符集为utf-8
            print(type(share_data))
            print(share_data)
            py_str = json.loads(share_data)  # 通过loads方法转化为python对象，然后进行相应的操作。
        except json.decoder.JSONDecodeError:
            print("wait it")
            time.sleep(3000)
        # print(json_str)
        print(type(py_str))
        print(py_str['feed'])
        py_lst = py_str['feed']
        i = 0
        print(len(py_lst))
        for i in range(len(py_lst)):
            print('*' * 100)
            print(i)
            print(py_lst[i]['title'])
            print(py_lst[i]['text'])
            print(py_lst[i]['uinfo']['province'])
            print(py_lst[i]['uinfo']['loc'])
            print(py_lst[i]['uinfo']['compos'])
            print(py_lst[i]['uinfo']['name'])
            print(py_lst[i]['uinfo']['career'])
            print(py_lst[i]['uinfo']['gender'])

            print(py_lst[i]['likes'])
            print(py_lst[i]['crtime'])
            with open('/tmp/maimai_word_activity.txt', "a+") as f:  # 把爬取的内容写入文件中
                f.write(
                    '*' * 100 + '\n' + py_lst[i]['title'] + '\n' + py_lst[i]['text'] + '\n' + py_lst[i]['uinfo'][
                        'province'] + '\n' + py_lst[i]['uinfo']['loc']
                    + '\n' + py_lst[i]['uinfo']['compos'] + '\n' + py_lst[i]['uinfo']['name'] + '\n' +
                    py_lst[i]['uinfo']['career'] + '\n' + str(py_lst[i]['uinfo']['gender']) + '\n' + str(
                        py_lst[i]['likes']) + '\n' + py_lst[i]['crtime'])
                f.write('\n')
        print("现在是第" + str(j) + "个翻页")
        j += 1




if __name__ == "__main__":
    parse_json()