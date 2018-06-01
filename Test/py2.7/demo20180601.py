#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180601.py
# Description      :
# Author         :Devon
# Date          :2018/6/1
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================


import sys
import difflib
try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    report = sys.argv[3]
except Exception,e:
    print ('Error:'+str(e))
    sys.exit()
def GetLines(file_name):
    return open(file_name).readlines()
txt_line1 = GetLines(file1)
txt_line2 = GetLines(file2)
print type(txt_line1)
d = difflib.HtmlDiff()
fid = open(report,'w')
fid.write(d.make_file(txt_line1,txt_line2))
fid.close()