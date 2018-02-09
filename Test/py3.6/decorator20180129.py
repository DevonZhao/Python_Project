#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : decorator20180129.py
# @Author  : devon
# @Date    : 2018/1/29
# @Platform: Mac
# @version :
# @Desc    : 


# 函数内的复习，部分可以略
# 设置递归限制
# import sys
# sys.setrecursionlimit(10)

def foo(x):
    print(locals())


f = foo(1)
print(f)


print(foo.__name__,foo.__doc__)


def outer(x):
    try:
        def inner():
            print("contents have been printed:{0}".format(x))
        inner()
        return outer(x)
    except Exception as e:   # python3的写法，python2则使用Exception,e:
        print(Exception, e)

outer(1)



# 下面说明装饰器：

import logging
def foo():
    print('i am foo')
    print(logging.info("foo is running."))

foo()

def use_logging(func):
    def wrapper(*args, **kwargs):   # 以传入任意数量的参数,任意数量的字典。
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@use_logging   # @用法
def bar():
    print("i am bar")

@use_logging
def foo():
    print("i am foo")

bar()
foo()

# def bar():
#     print("i am bar")
#
# bar = use_logging(bar)    # 直接引用用法
#
# bar()



# 这里例子更容易理解装饰器（另外一个实例）
import time

def test():
    time.sleep(2)
    print("test is running!")

def deco(func):
    start = time.time()
    print(start)
    func() #2
    stop = time.time()
    print(stop)
    print(stop-start)

deco(test) # 直接引用用法




# 对函数test的一个装饰，先test作为变量传递给函数deco里的参数，然后依次执行deco函数的内容。
print("*"*50,"the other example","*"*50)
def deco(func):
    start = time.time()
    print(start)
    func() #2
    stop = time.time()
    print(stop)
    print(stop-start)



@deco
def test():
    time.sleep(2)
    print("test is running!")
test



# 这里关注一下print和return的输出顺序。
def funct():
    print(1)
    print(2)
    return 3
print(funct())




def decorator(func):

    print('this is decorator')
    func()

@decorator
def target():
    print('this is target')


# TypeError: 'NoneType' object is not callable出现这样的错误后，就提示自己定义的装饰器不太合理，需要修改装饰器方法。
target  # 这里我们可以替换target和target()，这里要写target不会报错，但是改变了装饰器的初衷，不改变源代码，不改变调用。

#
# 装饰器在写法上和普通的函数有一点不同，装饰器要返回一个可调用的对象。
#
# 当()被附加在方法或者类后面时，表示调用，或者称为运行及实例化


# 改进后的装饰器，为了防止出现NoneType，是使用嵌套的方式。
def decorator(func):
    def restructure():
        func()
        print('this is decorator')
    return restructure

@decorator
def target():
    print('this is target')


target()

# 装饰带有参数的方法,这种自己可以设置多个参数。

def decorator(func):
    def restructure(*args):
        func(*args)
        print('this is decorator')
    return restructure

@decorator
def target(x):
    print('this is target %s'%x)

@decorator
def newtarget(x,y):
    print('this is target %s%s'%(x,y))

target('!')
newtarget('!','?')

# 带有参数的装饰器，写法为外面再嵌套一层，带有参数的方法。  这个典型的应用是，选择不同参数调用不同的被装饰函数。

print('*'*100)
def newdecorator(i):
    def decorator(func):
        def restructure(x):
            func(x)
            print('this is decorator %s%s'%(i,x))
        return restructure
    return decorator

@newdecorator('?')
def target(x):
    print('this is target %s'%x)

target('!')

# 参考文档：https://www.tuicool.com/articles/FBZvya