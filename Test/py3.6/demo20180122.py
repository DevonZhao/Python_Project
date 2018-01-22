#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : demo20180122.py
# @Author  : devon
# @Date    : 2018/1/22
# @Platform: Mac
# @version :
# @Desc    : 


d = {'x':1,'y':2,'z':3}
print(d)
for key in d:
    print(key,d[key])



'''
urllib is a package that collects several modules for working with URLs:
    urllib.request for opening and reading URLs
    urllib.error containing the exceptions raised by urllib.request
    urllib.parse for parsing URLs
    urllib.robotparser for parsing robots.txt files

'''

from urllib.parse import urlencode


# 1.在python3中urlencode被移到urllib.parse下
# 2.urllib.parse常用函数: urlencode,quote,quote_plus,unquote,unquote_plus

data = {'a':'test',
        'name':'魔兽'
        }
print(urlencode(data))

