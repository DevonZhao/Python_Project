#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : Binary_Search.py
# @Author  : devon
# @Date    : 2018/3/9
# @Platform: Mac
# @version :
# @Desc    : 二分查找算法python实现

"""

算法核心：在查找表中不断取中间元素与查找值进行比较，以二分之一的倍率进行表范围的缩小。


"""


def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印折半的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 99)
    print(result)





