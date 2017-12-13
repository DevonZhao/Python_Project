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
#==============================================================================


import os,sys
import MySQLdb

#
# print os.system('pwd')
#
# db = MySQLdb.connect("192.168.56.101","devon","123123", "mysql")
# cursor = db.cursor()
# cursor.execute("show all slaves status;")
# d = cursor.fetchall()
# print type(data),data
# db.close()

d = (('dn1', 'Slave has read all relay log; waiting for the slave I/O thread to update it', 'Waiting for master to send event', '10.10.5.6', 'repl', 8088L, 60L, 'binlog.000096', 69607055L, 'relay-bin-dn1.000083', 69607344L, 'binlog.000096', 'Yes', 'Yes', '', 'new_medic_assist.*,medic_assist.*,third_party_medic_assist.*,7lk_iplatform.nms_operation_log,rundeck.*', '', '', '', 'information_schema.%,performance_schema.%,mysql.%,test.%,salepromotion.%,sync_info.%,tungsten_gz_odc.%,tungsten_crm.%,fss.%,partner.%,pdc.%,permission.%,vorder.%,tungsten_pdc.%,base_commodity.%,baymax_doctor_weixin.%,bi_report.%,medic_assist.%,new_medic_assist.%,third_party_medic_assist.%,tungsten_migration_service.%,tungsten_ods33.%', 0L, '', 0L, 69607055L, 69607688L, 'None', '', 0L, 'No', '', '', '', '', '', 0L, 'No', 0L, '', 0L, '', '', 10100506L, '', '', 'No', '', '', '', 'conservative', 0L, 1073741824L, 3426748L, 0L, 1800.0, ''), ('dn2', 'Slave has read all relay log; waiting for the slave I/O thread to update it', 'Waiting for master to send event', '10.10.56.18', 'repl_to_slave', 3306L, 60L, 'binlog.000010', 501729699L, 'relay-bin-dn2.000029', 8503866L, 'binlog.000010', 'Yes', 'Yes', '', 'new_medic_assist.*,medic_assist.*,third_party_medic_assist.*,7lk_iplatform.nms_operation_log,rundeck.*', '', '', '', 'information_schema.%,performance_schema.%,mysql.%,test.%,salepromotion.%,sync_info.%,tungsten_gz_odc.%,tungsten_crm.%,fss.%,partner.%,pdc.%,permission.%,vorder.%,tungsten_pdc.%,base_commodity.%,baymax_doctor_weixin.%,bi_report.%,medic_assist.%,new_medic_assist.%,third_party_medic_assist.%,tungsten_migration_service.%,tungsten_ods33.%', 0L, '', 0L, 501729699L, 8504162L, 'None', '', 0L, 'No', '', '', '', '', '', 0L, 'No', 0L, '', 0L, '', '', 180L, '', '', 'No', '', '', '', 'conservative', 0L, 1073741824L, 73110L, 1L, 1800.0, ''), ('dn3', 'Slave has read all relay log; waiting for the slave I/O thread to update it', 'Waiting for master to send event', '10.10.5.4', 'repl', 3306L, 60L, 'binlog.000077', 854254501L, 'relay-bin-dn3.000061', 145961567L, 'binlog.000077', 'Yes', 'Yes', '', 'new_medic_assist.*,medic_assist.*,third_party_medic_assist.*,7lk_iplatform.nms_operation_log,rundeck.*', '', '', '', 'information_schema.%,performance_schema.%,mysql.%,test.%,salepromotion.%,sync_info.%,tungsten_gz_odc.%,tungsten_crm.%,fss.%,partner.%,pdc.%,permission.%,vorder.%,tungsten_pdc.%,base_commodity.%,baymax_doctor_weixin.%,bi_report.%,medic_assist.%,new_medic_assist.%,third_party_medic_assist.%,tungsten_migration_service.%,tungsten_ods33.%', 0L, '', 0L, 854254501L, 145961863L, 'None', '', 0L, 'No', '', '', '', '', '', 0L, 'No', 0L, '', 0L, '', '', 4L, '', '', 'No', '', '', '', 'conservative', 0L, 1073741824L, 316915L, 0L, 1800.0, ''), ('dn4', 'Slave has read all relay log; waiting for the slave I/O thread to update it', 'Waiting for master to send event', '10.10.1.254', 'repl', 3306L, 60L, 'binlog.003864', 708397964L, 'relay-bin-dn4.002511', 708398253L, 'binlog.003864', 'Yes', 'Yes', '', 'new_medic_assist.*,medic_assist.*,third_party_medic_assist.*,7lk_iplatform.nms_operation_log,rundeck.*', '', '', '', 'information_schema.%,performance_schema.%,mysql.%,test.%,salepromotion.%,sync_info.%,tungsten_gz_odc.%,tungsten_crm.%,fss.%,partner.%,pdc.%,permission.%,vorder.%,tungsten_pdc.%,base_commodity.%,baymax_doctor_weixin.%,bi_report.%,medic_assist.%,new_medic_assist.%,third_party_medic_assist.%,tungsten_migration_service.%,tungsten_ods33.%', 0L, '', 0L, 708397964L, 708398597L, 'None', '', 0L, 'No', '', '', '', '', '', 0L, 'No', 0L, '', 0L, '', '', 254L, '', '', 'No', '', '', '', 'conservative', 0L, 1073741824L, 22819012L, 0L, 1800.0, ''))
for i in range(len(d)):
    print "Connection_name: "+d[i][0]
    print "master server ip: "+d[i][3]
    print "Slave_IO_Running: " + d[i][12]
    print "Slave_SQL_Running: " + d[i][13]
    print "Seconds_Behind_Master: " + str(d[i][34])
    if d[i][12] is "Yes" and d[i][13] is "Yes":
        print 1
    else:
        print 0




