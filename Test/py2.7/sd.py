#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title          :change_mongo_format.py
# Desc           : change the format of the mongodb data.
# Author         :Devon
# Date           :2018/4/28
# Version        :1.0
# Platform       : windows
# Version        : 2.7.14
#==============================================================================

import os
import json

if os.path.exists('/tmp/drugs.csv'):
    print 'the drugs file already exits.it will been deleted.'
    os.system('rm -f /tmp/drugs.csv')
else:
    print 'The drugs file does not exist,continue.'

f = open("/tmp/medicationRemindNotify.json","r")
lines = f.readlines()
for line in lines:
    data = json.loads(line)
    for i in xrange(len(data['patientDrugs'])):
        for j in xrange(len(data['patientDrugs'][i]['medications'])):
            data_str = data['_id']['$oid']+','+data['doctorId']['$numberLong']+','+data['remindTime']['$numberLong']+','+\
            data['patientDrugs'][i]['patientId']['$numberLong']+','+data['patientDrugs'][i]['recommandId']['$numberLong']+','+data['patientDrugs'][i]['createdAt']['$numberLong']+','+\
            data['patientDrugs'][i]['medications'][j]['skuid']['$numberLong']+','+data['patientDrugs'][i]['medications'][j]['spec']+','+\
            data['patientDrugs'][i]['medications'][j]['name']+','+data['patientDrugs'][i]['medications'][j]['endTime']['$numberLong']
            with open("/tmp/drugs.csv", "a") as f:
                f.write(data_str.encode("utf8")+'\n')




