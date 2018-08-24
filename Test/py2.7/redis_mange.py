#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :redis_mange.py
# Description      : 查看redis中的key是否设置了过期时间，有多少设置了。
# Author         :Devon
# Date          :2018/7/18
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

import redis
r = redis.StrictRedis(host='10.9.2.13',password='7lkddfdfdff223D', port=6379, db=0)
ret = r.scan_iter()
i  = 0
for a in ret:
    # print r.get(a),r.ttl(a)
    if r.ttl(a) == -1:
        i = i +1
    if r.ttl(a) <> -1:
        print a
print i
    # print r.pttl(a)
    # print r.ttl(a)


# print help(r)
