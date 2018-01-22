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
# ==============================================================================


a = '   123'
print a.strip()
a = '\t\t\n\tabc'
print a

# list operation and example.

lst = ['devon1', 'devon2', 'devon3', 'devon4']
lst.reverse()    # reverse a list.
print lst
print lst.append(lst[0])   # add new object after the list
print lst.count('devon4')   #
print lst
print lst[0]

# string example

str = 'this is a string example'

print str
print type(str)

new_str = str.strip()
print new_str
print str.split()   # string change to list
