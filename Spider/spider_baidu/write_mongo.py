#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : write_mongo.py
# @Author  : devon
# @Date    : 2018/2/3
# @Platform: Mac
# @version :
# @Desc    : 


import pymongo
# from get_key_contents import FindRecord  # 引用刚刚定义的包

server_ip = "192.168.56.142"
port = 27017

def conn_mongo():
    mc = pymongo.MongoClient(server_ip, port)
    db = mc.spiderdb
    col = db.key_list
    # return col

