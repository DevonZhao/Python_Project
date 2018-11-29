#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :test1129.py
# Description      :
# Author         :Devon
# Date          :2018/11/29
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================\



import re

str2 = '''

// 测试

CREATE TABLE `t1` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主建',
  `type` int(2) DEFAULT NULL COMMENT '类型',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='1';

# 测试
alter TABLE t2 add(
  `status` tinyint(1) default '1' COMMENT '是否有效(0：否，1：是)'
);

'''


def stripComments(code):
    code = str(code)
    return re.sub(r'(?m)^ *(#|//|--).*n?', '', code)

print(stripComments(str2))

