#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180227.py
# Description      :
# Author         :Devon
# Date          :2018/2/27
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/apistore/dhc/getalltemplate?user=640ea6c0ffc2dd5dea3435f95d7b477e'
req = urllib2.Request(url)

req.add_header("apikey", "640ea6c0ffc2dd5dea3435f95d7b477e")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)