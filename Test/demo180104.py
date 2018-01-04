#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :test4.py
# Description      :I am test script
# Author         :Devon
# Date          :2018/01/04
# Version        :0.1
# Usage         :python test4.py
# Notes         :
# python_version     :2.7.14
# ==============================================================================

'''
requests的几个重要方法
    get方法
        get方法里面的可选参数：
            params={'wd': 'python'} 字典形式
            -------------------------------------
            timeout=1
            headers=headers
            cookies=cookies  cookies是预先定义好的。
            proxies=proxies 设置代理，字典格式预先定义好。
        .status_code #返回状态
        .raise_for_status() #失败请求(非200响应)抛出异常
        .encoding = 'UTF-8' #设置字符集
        .headers 获取响应头

        响应内容：
            .raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
            .content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
            .text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码



    post方法
        get方法里面的可选参数：
            data 发送一些参数为表单形式的数据
            json=
            -----------------------------
            files=

设置字符集：
    如果打印的出来的内容是乱码的，可以设置字符集，通过
    r.encoding='utf8'或者
    headers = {'content-type':'text/html; charset=utf-8'}

'''


import requests

r = requests.get(url='http://baidu.com')  #简单的get方法使用
print r.status_code
# r = requests.get(url='http://www.baidu.com/s?', params={'wd': 'python'})   # 带有参数的get方法
print r.url
print r.text
r.encoding = 'utf8'
print r.encoding
print r.content

r_json = requests.get('https://github.com/timeline.json')
print r_json.json()
bad_r = requests.get('http://httpbin.org/status/404')
print bad_r.status_code
print bad_r.raise_for_status()

payload = {'key1': 'value1', 'key2': 'value2'}

r_post = requests.post("http://httpbin.org/post", data=payload)   # 发送一些编码为表单形式的数据
print r_post.text



