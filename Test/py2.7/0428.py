#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :0428.py
# Description      :
# Author         :Devon
# Date          :2018/4/28
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

import os
import json

os.system('rm -f /tmp/open.txt')
f = open("/root/medicationRemindNotify.json","r")
lines = f.readlines()
for line in lines:
    data = json.loads(line)
    # print data

    # print data['_id']['$oid'],data['doctorId']['$numberLong'],data['remindTime']['$numberLong']
    # print data['patientDrugs']

    for i in xrange(len(data['patientDrugs'])):
        # print data['_id']['$oid'],data['doctorId']['$numberLong'],data['remindTime']['$numberLong'],data['patientDrugs'][i]['patientId']['$numberLong'],\
        #     data['patientDrugs'][i]['recommandId']['$numberLong'],data['patientDrugs'][i]['createdAt']['$numberLong']
        # print data['patientDrugs'][i]['medications']
        for j in xrange(len(data['patientDrugs'][i]['medications'])):
            print data['_id']['$oid']+','+data['doctorId']['$numberLong']+','+data['remindTime']['$numberLong']+','+\
            data['patientDrugs'][i]['patientId']['$numberLong']+','+data['patientDrugs'][i]['recommandId']['$numberLong']+','+data['patientDrugs'][i]['createdAt']['$numberLong']+','+\
            data['patientDrugs'][i]['medications'][j]['skuid']['$numberLong']+','+data['patientDrugs'][i]['medications'][j]['spec']+','+\
            data['patientDrugs'][i]['medications'][j]['name']+','+data['patientDrugs'][i]['medications'][j]['endTime']['$numberLong']

            data_str = data['_id']['$oid']+','+data['doctorId']['$numberLong']+','+data['remindTime']['$numberLong']+','+\
            data['patientDrugs'][i]['patientId']['$numberLong']+','+data['patientDrugs'][i]['recommandId']['$numberLong']+','+data['patientDrugs'][i]['createdAt']['$numberLong']+','+\
            data['patientDrugs'][i]['medications'][j]['skuid']['$numberLong']+','+data['patientDrugs'][i]['medications'][j]['spec']+','+\
            data['patientDrugs'][i]['medications'][j]['name']+','+data['patientDrugs'][i]['medications'][j]['endTime']['$numberLong']
            print data_str
            print type(data_str.encode("gbk"))

            with open("/tmp/open.txt", "a") as f:
                f.write(data_str.encode("utf8")+'\n')




