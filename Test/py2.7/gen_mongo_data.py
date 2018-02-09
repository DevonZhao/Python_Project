
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :gen_mongo_data.py
# Description      :
# Author         :Devon
# Date          :2018/2/2
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

i = 1
for i in range(5000,5500):

    print 'db.user.insert({"username": "test%d", "age": "%d", "sex": "f"});' %(i,i)

