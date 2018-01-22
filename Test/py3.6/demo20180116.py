#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : demo20180116.py
# @Author  : Devon
# @Date    : 2018/1/16
# @Platform: Mac
# @version :
# @Desc    :


'''

总结：
1.赋值：简单地拷贝对象的引用，两个对象的id相同。
2.浅拷贝：创建一个新的组合对象，这个新对象与原对象共享内存中的子对象。
3.深拷贝：创建一个新的组合对象，同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。
4.浅拷贝和深拷贝的不同仅仅是对组合对象来说，所谓的组合对象就是包含了其它对象的对象，如列表，类实例。而对于数字、字符串以及其它“原子”类型，没有拷贝一说，产生的都是原对象的引用。
5.对于可变对象来说：
    浅copy：父对象不同，子对象相同
    深copy：父对象和子对象均不同


'''

import copy

# 对于不可变类型深copy是一样的，不会是两个对象。

a = [1,2,3]
print(type(a[0]))
print(isinstance(a[0],int))  # 判断一个变量是不是int类型
b = copy.deepcopy(a)
print(id(a),id(b))
for x,y in zip(a,b):
    print(id(x),id(y))
    print(x,y)


print("*"*100)
a1 = [[1,2],[5,6],[8,9]]
b1 = copy.copy(a1)
c1 = copy.deepcopy(a1)
print(id(a1),id(b1))
for x1,y1 in zip(a1,b1):
    print(id(x1),id(y1))

print("")
print(id(a1),id(c1))
for x1,y1 in zip(a1,c1):
    print(id(x1),id(y1))



# 下面是关于常用函数复习
# 在python3中要得到filter等函数的结果要使用list。list(map(f1, l1, l2))
def f(x):
    return x%2!=0 and x%3!=0

print(list(filter(f,range(2,25))))


def cube(x):
    return x*x*x

print(list(map(cube,range(1,11))))


def add(x,y):
    return x+y

print(list(map(add,range(8),range(8))))

from functools import reduce
print(reduce(lambda x,y:x+y,range(101)))   # 这里不需要使用list()

