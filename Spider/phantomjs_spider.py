#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :phantomjs_spider.py
# Description      :
# Author         :Devon
# Date          :2018/2/11
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================
import urllib2,re,os,datetime
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
browser = webdriver.PhantomJS(executable_path=r'/pyapp/phantomjs-1.9.8/bin/phantomjs',desired_capabilities=dcap)
browser.get(url)
time.sleep(3)
print(browser.find_element_by_id("contents").text)
browser.save_screenshot("1.png")  # 截图保存
browser.close()
browser.quit()