#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : spider.py
# @Author  : devon
# @Date    : 2018/2/7
# @Platform: Mac
# @version :
# @Desc    :


from bs4 import BeautifulSoup
import re
import requests
import base64
import urllib
import rsa
import json
import binascii
import string
import random
import time
import logging, logging.handlers

def userlogin(username, password):
    session = requests.Session()
    url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=account&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.18)&_=1518075753189'
    # https://login.sina.com.cn/signup/signin.php?entry=sso
    url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)&_=1518075753189'

    #如何得到response后的结果。
    # get servertime,nonce, pubkey,rsakv
    resp = session.get(url_prelogin)
    print(resp.text)
    p = re.compile('{.*}')
    json_data = re.findall(p, resp.text)[0]
    print(json_data)
    data = json.loads(json_data)

    # print(json_data,type(json_data))
    # data = eval(json_data)
    servertime = data['servertime']
    print('servertime:', servertime)
    nonce = data['nonce']
    pubkey = data['pubkey']
    rsakv = data['rsakv']
    retcode = data['retcode']
    if retcode!=0:
        print(retcode)
    else:
        print(0)



    # calculate su
    urllib.parse.quote(username)   # 屏蔽特殊的字符、比如如果url里面的空格！url里面是不允许出现空格的。
    su = base64.b64encode(username.encode(encoding="utf-8"))
    # calculate sp
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537)
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    sp = binascii.b2a_hex(rsa.encrypt(message.encode(encoding="utf-8"), key))
    postdata = {
        'entry': 'account',
        'gateway': '1',
        'from': '',
        'savestate': '30',
        'userticket': '0',
        'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': su,
        'service': 'account',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'sp': '9912a6d0151648729ac902853f6c25f43f13210fca121d4c4c3d72b7d076e24d6bf543fd4e7f54c011a6fb09efe422c05b68b746f0ac771e1ff23b2c7a7ca28edf33bd2e84348bdcdbf5a7bbef77b76fdb50e6b7f08a26ad147ecbd5655e69a49a58681f1887b1695ee1a845c6a289232b4c113b22ec8ea495a8c37ab4cee080',
        'encoding': 'UTF-8',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META',
        'rsakv': rsakv,
    }

    print(postdata)
    resp = session.post(url_login, data=postdata)
    # print resp.headers

    print("*"*100)
    print(resp.text)

    login_url = re.findall(r'http:/weibo.*&retcode=.*', resp.text)
    print('login_url', login_url, type(login_url))
    respo = session.get(login_url[0])
    uid = re.findall('"uniqueid":"(\d+)",',respo.text)[0]
    url = "http://weibo.com/u/"+uid
    respo = session.get(url)

    print(respo.text)

userlogin('18650306405', 'lkz881199')


def parse_contents():
    url = 'https://weibo.com/1712570933/G1SP7e6es?ref=feedsdk&type=comment#_rnd1517975034357'
    headers = {
                'Cookie': 'userProvinceId=2; userCityId=0; userLocationId=26; proIp=123; ip_ck=4cKD5vP/j7QuNjUyMTk4LjE0Njk0Mzg5MzQ%3D; lv=1469438963; vn=1; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1469438964; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1469438964; z_day=rdetail=1; z_pro_city=s_provice%3Dshanghai%26s_city%3Dxingqu',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
            }
    content = requests.get(url, headers).text
    st_code = requests.get(url, headers).status_code
    print(st_code)
    print(content)
    # try:
    #             r=requests.get(url,proxies=prox,headers=header)
    #             if r.status_code!=200:
    #                 continue
    #             else:
    #                 print "使用{0}连接成功>>".format(prox)
    #                 return r.content
    #         except Exception, e:
    #             return None

    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    # print(content)
    # print(soup)
    if st_code:
        c = soup.find_all(name="div")
        # print(c)