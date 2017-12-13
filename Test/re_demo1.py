#! _*_ coding: utf-8 _*_
import re

def find_start_imooc(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc'):
            print line

find_start_imooc('/pyapp/file/imooc.txt')


str1 = 'imooc python'
str1.find('imooc')
pa = re.compile(r'imooc')  #先使用compile生成一个Pattern对象，然后使用match进行匹配
ma = pa.match(str1)

str2 = 'abc'
pa2 = re.compile(r'a.c')
ma2 = pa2.match(str2)
print ma2.group()

#通过正则表达式来匹配邮箱地址
import re
def get_email():
    text = input("Please input your email address:\n")
    if re.match(r'^\w{0,19}\W{0,19}@\w{1,13}\.[com,cn,gov]{1,3}$', text):    #{0,19}这里表示限制长度
        print "your email is right."
    else:
        print "you enter a wrong email,please enter again."

#通过正则表达式来匹配IP地址
def get_ip():
    ip = input("please enter the ip address of your server: \n ")
    if re.match(r'\d\.\d\.\d\.\d', ip):
        print "your ip is right"
    else:
        print "error"


if __name__ == '__main__':
    get_email()
    get_ip()





