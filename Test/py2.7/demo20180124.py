#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180124.py
# Description      : 连接mongo创建测试数据
# Author         :Devon
# Date          :2018/1/24
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py
# python_version     :2.7.14
#==============================================================================

import pymongo
import random
import string
conn = pymongo.MongoClient('192.168.56.142',27017)
db = conn.modb
reg_info = db.reg_info
i = 0
while i < 1000:
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))   # 生成随机字符串
    ran_age = random.randint(1, 100)  # 生成1--100随机整数
    if ran_age % 2 == 0:
        gender = "man"
    else:
        gender = "woman"
    reg_info_dict = {"name":ran_str, "age":ran_age, "gender":gender}
    reg_info.insert(reg_info_dict)
    i += 1