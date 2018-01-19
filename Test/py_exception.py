#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :py_exception.py
# Description      :
# Author         :Devon
# Date          :2018/1/17
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================
# 各个异常处理解释
try:
    x = int(input('input x:'))
    y = int(input('input y:'))
    print('x/y = ',x/y)
except ZeroDivisionError: #捕捉除0异常
    print("ZeroDivision")
except (TypeError,ValueError) as e: #捕捉多个异常
    print(e)
except: #捕捉其余类型异常
    print("it's still wrong")
else:  #没有异常时执行
    print('it work well')
finally: #不管是否有异常都会执行
    print("Cleaning up")

i =0
f = lambda x,y:x+y   # 定义lambda函数

# 实例使用try .. except .. else进行输入三次数字，错误类型就跳出。
while i < 3:
    try:
        num1 = int(input("please enter a number:"))
        num2 = int(input("please enter the second number:"))
        print "这两个数的和为：",f(num1, num2)
    except ValueError:
        print "You enter the error value."
        i += 1
        print i
        if i >=3:
             print "失败次数过多。"
        continue
    else:
        print "there is no error in the code."
        break
    finally:
        pass







