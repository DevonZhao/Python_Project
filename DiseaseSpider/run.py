#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : run.py
# @Author  : devon
# @Date    : 2018/1/23
# @Platform: Mac
# @version :
# @Desc    : 


from scrapy import cmdline


name = 'disease'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())