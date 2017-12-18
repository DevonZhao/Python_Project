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
#==============================================================================

'''




'''


import numpy as np

print np.version.version  # 打印numpy的版本

# 数组操作：
# 1.数组的创建
#以list或tuple为变量参数产生一维数组
print np.array([1,2,3,4])
print np.array((1.2,2,3,4))

# 以list或tuple变量为元素产生二维数组
print np.array([[1,2],[3,4]])

print np.array((1.2,2,3,4),dtype=np.int32) # 生成数组的时候，可以指定数据类型，例如numpy.int32, numpy.int16, and numpy.float64等

print np.arange(15)
print type(np.arange(15))
print np.zeros((3, 6))
print np.arange(12).reshape((3,4))  #更改shappe使用reshape ，产生什么样的数组
print np.linspace(1,10,6) #生成线段

# numpy数学运算
a = np.array([10,20,30,40])
b = np.arange(4)
print a,b
c1 = a - b
print c1
c2 = a + b
print c2
c3 = b **4 #平方
print c3

print b < 3

#二维矩阵的运算

a1 = np.array([[1,1],[0,1]])
b1 = np.arange(4).reshape((2,2))

c4 = a1*b1
c4_dot = np.dot(a1,b1)  #另外的一种方式：a.dot(b)
print c4
print c4_dot

#numpy聚合操作（sum,min,max）
ra = np.random.random((2,5))
print type(ra)
print ra
print np.sum(ra, axis=1) #每一列求和,ra就是上面定义的。
print np.min(ra, axis=0) #每一行寻找最小值
print np.max(ra,axis=1)

