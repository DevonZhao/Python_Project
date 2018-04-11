#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180302.py
# Description      : Monitor change of the Mysql user's infomation change
# Author         :Devon
# Date          :2018/3/2
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================


import MySQLdb
# sql = 'select user,host,password from mysql.user;'
# conn = MySQLdb.Connect('192.168.56.142','3306','','')
# contents = conn.query(sql)
# print contents
t_pre = 'consult_bill'
new_db_name = 'baymax_out'
sql = 'select mod(doctor_id,128),doctor_id from  (select DISTINCT doctor_id from baymax.consult_bill) a;'
db = MySQLdb.Connect('10.10.192.33','dbadmin','1qaz2wsx')
cursor = db.cursor()
cursor.execute(sql)
data = cursor.fetchall()
# print  data
# # data = list(set(data))
# print data

for d in data:
    sub_table_name = t_pre + '_' + str(int(d[0]) + 1).zfill(3)
    # print sub_table_name
    new_sql = 'insert into %s.%s(patient_id,doctor_id,amount,pay_amount,discount_amount,resource_type,created_at,pay_time,pay_status,pay_type,third_type,balance_pay,third_pay) select patient_id,doctor_id,amount,pay_amount,discount_amount,resource_type,created_at,pay_time,pay_status,pay_type,third_type,balance_pay,third_pay from baymax.consult_bill where doctor_id= %s; '%(new_db_name,sub_table_name,int(d[1]))
    print new_sql
    cursor.execute(new_sql)
    db.commit()
# print data
db.close()
t_pre = 'consult_bill'
i = 0
for i in range(128):
    sub_table_name = t_pre+'_'+str(i+1).zfill(3)
    # print sub_table_name
    create_table_sql = '''
    CREATE TABLE consult_bill_%s(
      `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
      `patient_id` bigint(20) NOT NULL COMMENT '患者id',
      `doctor_id` bigint(20) NOT NULL COMMENT '医生id',
      `amount` int(11) NOT NULL DEFAULT '0' COMMENT '应付金额，单位：分',
      `pay_amount` int(11) NOT NULL DEFAULT '0' COMMENT '实付金额，单位：分',
      `discount_amount` int(11) NOT NULL DEFAULT '0' COMMENT '抵扣金额，单位：分',
      `resource_type` int(1) NOT NULL COMMENT '来源类型，0：正常；1：免单；2：未开启收费；3：医生主动发起',
      `created_at` datetime DEFAULT NULL COMMENT '账单创建时间',
      `pay_time` datetime DEFAULT NULL COMMENT '支付时间',
      `pay_status` int(1) NOT NULL DEFAULT '0' COMMENT '支付状态，0：未支付；1：已支付',
      `pay_type` int(1) NOT NULL DEFAULT '0' COMMENT '支付方式   1：余额支付；2：第三方支付；3：组合支付',
      `third_type` int(1) NOT NULL DEFAULT '0' COMMENT '第三方类型   0：未知； 1：微信',
      `balance_pay` int(11) NOT NULL DEFAULT '0' COMMENT '余额支付数额，单位：分',
      `third_pay` int(11) NOT NULL DEFAULT '0' COMMENT '第三方支付金额，单位：分',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='账单信息表';''' % (str(i + 1).zfill(3))


