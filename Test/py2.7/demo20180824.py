#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180824.py
# Description      :
# Author         :Devon
# Date          :2018/8/24
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================


import os,sys

str='group1/M00/00/C5/wKgBt1XUMRyAKNn-AAuD5uoie-g521.png,group1/M00/1B/EF/wKgBuFXUMRyAEwADAAzBDj4fT54944.png,group1/M00/00/C5/wKgBt1XUMRyAJMclAAmWUeptZHw620.png'

print ','.join([x.split('/')[-1] for x in str.split(',')])

# print str.split(',')[0].split('/')[-1]


for x in str.split(','):
    print x.split('/')[-1]