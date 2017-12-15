#! /usr/bin/env python
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

import re
import requests
import codecs
import time
import random
from itertools import izip
import lxml
from bs4 import BeautifulSoup


head_url = 'http://vcbeat.net/VB100'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}

html = requests.get(head_url, headers=header).content
soup = BeautifulSoup(html,'lxml')

jiabin = soup.select('.jiabing > li')
i = 0
print len(jiabin)
while range(len(jiabin)):
    print "*" * 30
    print "当前是第 %s 个特邀嘉宾: "%(i+1)
    print "联系人："+ jiabin[i].select('.p1')[0].get_text().encode('utf8')
    print "所属公司："+ jiabin[i].select('.p2')[0].get_text().encode('utf8')
    i += 1
    if i >= len(jiabin):
        break

'''
<a href="/VB100/3" target="_blank">
                            <div class="con_ft">独角兽论坛</div>
                            <img src="/Application/Index/View/Computer/Public/img/Show/con0.png" />
                        </a>
'''

con_img = soup.select('.con_img')
while_list =  con_img[0].select('a')
j = 0
while range(len(while_list)):
    h = con_img[0].select('a')[j]['href']
    print h
    url_suf = h.split('/')[-1]

    ch_url = head_url+'/'+url_suf
    ch_html = requests.get(ch_url, headers=header).content
    ch_soup = BeautifulSoup(ch_html, 'lxml')
    jb = ch_soup.select('.jb > li')
    x = 0
    while range(len(jb)):
        print "*" * 30
        print "当前是第 %s 个特邀嘉宾: " % (x + 1)
        print "联系人：" + jb[x].select('.p1')[0].get_text().encode('utf8')
        print "所属公司：" + jb[x].select('.p2')[0].get_text().encode('utf8')
        x += 1
        if x >= len(jb) -1:
            break
    print ch_url
    j += 1
    if j >= len(while_list):
        break
# print con_img






# d = soup.find_all('p')
# tag = soup.p
# tag2 = tag.contents
#
# print tag2[0]
# name = soup.select('.p1')
# s = str(name)
# print s.decode("unicode-escape")
# print name
# print "###############################"
# l = soup.select('li')
#
# # print l
# #
# s1 = list(l)
#
# # print s1
#
# for i in s1:
#     str_i = str(i)
#     # print "tesddddddddddd"+str_i
#     if re.match('[class]', str_i) == 'None':
#          print 'match it'
#     else:
#         print str_i+'dddddddddddddddddddddd'
#
# # print s1.decode("unicode-escape")
# # for i in l:
# #     if re.match('[class]', str(i)) == 'None':
# #         print i
#
#
#     # if str() == 'None':
#     #     pass
#     # else:
#     #     print i
#
#
# # s1 = str(l)
# # print s1.decode("unicode-escape")
# #

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    comment_list = soup.select('.comment > p')
    next_page = soup.select('#paginator > a')[2].get('href')
    date_nodes = soup.select('..comment-time')
    return comment_list,next_page,date_nodes


