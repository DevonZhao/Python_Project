#!/usr/local/env3.6/bin/env python
# -*- coding: utf-8 -*-
# @File    : demo20180409.py
# @Author  : devon
# @Date    : 2018/4/9
# @Platform: Mac
# @version :
# @Desc    : 

# 在一个序列中找出出现次数最多的两个元素。

str = 'abcdfderfdfaqobaat'

from collections import Counter
c = Counter(str)
c.most_common(3)
print(c.most_common(3))

counter = {}
for i in str:
    counter[i] = counter.get(i,0)+1

print(counter)
print(sorted([(freq, word) for word, freq in counter.items()], reverse=True)[0])



