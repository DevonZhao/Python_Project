#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :spider_fang.py
# Description      :
# Author         :Devon
# Date          :2018/2/11
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================
# 爬取搜房网的www站点有些限制，使用m.fang.com来进行爬取。相关内容见demo20180209.py


# 爬取评论数，最新评论时间，户型，
import sys
import requests
import re
from bs4 import BeautifulSoup
import random
import pymongo
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
url = 'http://m.fang.com/xf/bj/'
server_ip = "192.168.56.142"
port = 27017
def rand_header():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11',
                       'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0'
                       ]
    result = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return result

def ge_url_list():
    i = 1
    while i <= 10:
        params = {'m': 'xflist', 'p': i}
        header = rand_header()
        html = requests.post(url, data=params, headers=header, verify=False)
        encode_content = html.content
        soup = BeautifulSoup(encode_content, 'lxml')
        fang_url_post = soup.find_all("a", href=re.compile("xf"))
        url_list = []
        for i in range(len(fang_url_post)):
            fang_url = fang_url_post[i]['href']
            if re.match(r'h+', fang_url):
                if re.match(r'^http', fang_url):
                    print fang_url
                    url_list.append(fang_url)
                else:
                    fang_url = "http:" + fang_url_post[i]['href']
                    print fang_url
                    url_list.append(fang_url)

        i = i + 1
        return url_list

def get_detail_info():
    url_list = ge_url_list()
    for url_var in url_list:
        print url_var
        header = rand_header()
        html = requests.get(url_var, headers=header, verify=False)
        encode_content = html.content
        soup = BeautifulSoup(encode_content,'lxml')
        item_name = soup.find_all("div", attrs={"class": re.compile(r'tit')})[0].contents[0]
        post_time = soup.find_all("span", attrs={"class": "time"})[0].contents[0]
        count = int(soup.find_all("i", attrs={"class": "f13"})[0].contents[0].replace(r"（","").replace(r"）",""))
        print "楼盘名："+item_name
        print "评论时间："+post_time
        print "评论数量："+str(count)
        detail_url = "http://m.fang.com"+soup.find_all("a", attrs={"class": re.compile(r'btn-more2 blue-arr-rt3')})[0]["href"]
        print detail_url
        detail_info = requests.get(detail_url, headers=header, verify=False)
        detail_content = detail_info.content
        detail_soup = BeautifulSoup(detail_content, 'lxml')
        li_detail = detail_soup.find_all("li")
        # print li_detail
        for li in range(len(li_detail)):
            # print li_detail[li]
            try:
                col_name = li_detail[li].span.contents[0]
                col_value = li_detail[li].p.contents[0]
                print col_name,col_value
            except Exception as e:
                pass


def conn_mongo():
    mc = pymongo.MongoClient(server_ip, port)
    db = mc.spiderdb
    col = db.house_info
    col.insert({"title": a2_tittle, "url": a2_url, "content": a1, "keyword":kw1})

if __name__ == "__main__":
    get_detail_info()




