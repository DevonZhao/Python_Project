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

student = Student()

# 上面一种
student.age    # 返回 25
student.age()  # 25是数字不是函数，不能执行，报错

# 下面一种
student.age    # 返回匿名函数
student.age()  #  执行这个匿名函数，返回25
