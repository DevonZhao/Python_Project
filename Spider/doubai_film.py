#! /usr/lib/env2.7/bin/python
# -*- coding: utf-8 -*-
# Title         :test4.py
# Description      :I am test script
# Author         :Devon
# Date          :20160902
# Version        :0.1
# Usage         :python test4.py
# Notes         : 通过bs4抓取豆瓣上的电视剧的短评
# python_version     :2.7.14

import re
import requests
import codecs
import time
import random
from itertools import izip
from bs4 import BeautifulSoup
absolute = 'https://movie.douban.com/subject/26605881/comments'
absolute_url = 'https://movie.douban.com/subject/26605881/comments?start=20&limit=20&sort=new_score&status=P&percent_type='
url = 'https://movie.douban.com/subject/26322642/comments?start={}&limit=20&sort=new_score&status=P'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}
def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    comment_list = soup.select('.comment > p')
    next_page= soup.select('#paginator > a')[2].get('href')
    date_nodes = soup.select('..comment-time')
    return comment_list,next_page,date_nodes

def get_cookies():
    f_cookies = open('/pyapp/file/cookie.txt', 'r')
    cookies = {}
    for line in f_cookies.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    return cookies

def record_comment():
    cookies = get_cookies()
    html = requests.get(absolute_url, cookies=cookies, headers=header).content
    # 获取评
    comment_list, next_page, date_nodes = get_data(html, )
    i = 0
    while (next_page != []) and i < 2000000:  # 查看“下一页”的A标签链接， while多个条件同时满足使用and
        print(absolute + next_page)
        html = requests.get(absolute + next_page, cookies=cookies, headers=header).content
        comment_list, next_page, date_nodes = get_data(html)
        with open("comments.txt", 'a')as f:
                for node, date in izip(comment_list, date_nodes):   #对两个list进行迭代izip
                    comment = node.get_text().strip().replace("\n", "")
                    date = date.get_text().strip()
                    print comment, date
                    content = comment.encode('utf-8') + date.encode('utf-8') + '\n'
                    f.writelines(content)
        i += 1
        print
        # if i > 2:
        #     break
        time.sleep(1 + float(random.randint(1, 100)) / 20)

if __name__ == '__main__':
    record_comment()


