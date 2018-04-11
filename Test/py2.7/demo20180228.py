#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180228.py
# Description      :
# Author         :Devon
# Date          :2018/2/28
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

import pymongo

from pymongo import MongoClient

conn = MongoClient('192.168.56.142', 27017)
db = conn['admin']
db.authenticate("root", "root")
conn.server_info()
conn.get_database("config").collection_names()
if "system.sessions" in conn.get_database("config").collection_names():
    print "ok"
else:
    print "error"
print conn.get_database("config").collection_names()


di = {}

