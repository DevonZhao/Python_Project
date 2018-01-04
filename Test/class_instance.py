#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :test4.py
# Description      :I am test script
# Author         :Devon
# Date          :2018-01-04
# Version        :0.1
# Usage         :python test4.py
# Notes         :
# python_version     :2.7.14
# ==============================================================================
'''

类和实例(class和instance)：
	1.类：类是抽象的模板，如如Student类，类型为类<class '__main__.Student'>
	2.实例：实例是类创建出来的一个个的具体对象，对象有相同方法，但是里面具体数据可能不同。类型为object。<__main__.Student object at 0x7f346359b390>

	3.区别：
		Student()是实例对象
		Student就是类

	4.__init__方法是类实例创建之后调用, 对当前对象的实例的一些初始化, 没有返回值


函数：
	函数和类中方法区别：
		类的方法的第一个参数永远是实例变量self，调用是不需要传递这个参数。其他和普通函数没有区别。

	区别：
		test_fun()是str类型，可以看成对象
		test_fun就是函数


'''


class Student(object):
    def __init__(self):
        pass


student = Student()
student2 = Student()
student.name = 'devon'
print student.name
print Student
print student2
print Student()


def test_fun():
    print "test function"
    return "yes"


print test_fun()

print type(test_fun())
# print test_fun
print type(test_fun)


import os


# 定义一个类，初始化id和name，然后定义个方法，让用户输入name，然后打印输入的名字

class Job(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_user_name(self):
        name_input = input("Please enter your name:")
        print name_input

job = Job(1, 'devon')  # 在实例化的时候要输入参数
print job.id, job.name
print job.get_user_name()   # 调用class的方法
