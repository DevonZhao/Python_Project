#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Title         :demo20180411.py
# Description      :
# Author         :Devon
# Date          :2018/4/11
# Version        :1.0
# Platform       : windows
# Usage         :python test4.py

# python_version     :2.7.14
#==============================================================================

import pymongo


# def insert_data():
client = pymongo.MongoClient("10.10.48.203:27017")
db = client["baymaxIm"]
db_coll = db["m_session" ]
insertArgs = {
        "_class" : "com.qlk.cloud.baymax.im.network.protocl.SessionDetails",
        "fromId" : 16664,
        "toId" : 73752,
        "endTime" : 1450160675085,
        "relation" : 1,
        "payStatus" : 1,
        "price" : "0",
        "lastMsg" : {
                "type" : 16,
                "content" : {
                        "recommandId" : 23127,
                        "items" : [
                                {
                                        "spec" : "0.17g*60片/盒",
                                        "productId" : 5004,
                                        "skuId" : 22729,
                                        "productName" : "方盛 血塞通分散片  60片*0.17g/片",
                                        "quantity" : 1,
                                        "usage" : "一天3次,一次2片,饭后服用,口服",
                                        "bakup" : "",
                                        "commonName" : "血塞通分散片"
                                }
                        ]
                }
        },
        "firstMsg" : {
                "type" : 16,
                "content" : {
                        "_class" : "com.qlk.cloud.baymax.im.network.protocl.RecommandDrug",
                        "recommandId" : 16911,
                        "items" : [
                                {
                                        "spec" : "0.17g*60片/盒",
                                        "productId" : 5004,
                                        "skuId" : 22729,
                                        "productName" : "方盛 血塞通分散片  60片*0.17g/片",
                                        "quantity" : 1,
                                        "usage" : "一天3次,一次2片,饭后服用,口服",
                                        "bakup" : "",
                                        "commonName" : "血塞通分散片"
                                }
                        ]
                }
        },
        "containRecom" : 1,
        "containVideo" : 0,
        "sessionId" : "16664_73752_1448348944355",
        "beginTime" : 1448348944355,
        "payType" : 0
}
for j in xrange(100,3000):
    db_coll.insert({'_id':j ,"_class" : "com.qlk.cloud.baymax.im.network.protocl.SessionDetails",
            "fromId" : 16664,
            "toId" : 73752,
            "endTime" : 1450160675085,
            "relation" : 1,
            "payStatus" : 1,
            "price" : "0",
            "lastMsg" : {
                    "type" : 16,
                    "content" : {
                            "recommandId" : 23127,
                            "items" : [
                                    {
                                            "spec" : "0.17g*60片/盒",
                                            "productId" : 5004,
                                            "skuId" : 22729,
                                            "productName" : "方盛 血塞通分散片  60片*0.17g/片",
                                            "quantity" : 1,
                                            "usage" : "一天3次,一次2片,饭后服用,口服",
                                            "bakup" : "",
                                            "commonName" : "血塞通分散片"
                                    }
                            ]
                    }
            },
            "firstMsg" : {
                    "type" : 16,
                    "content" : {
                            "_class" : "com.qlk.cloud.baymax.im.network.protocl.RecommandDrug",
                            "recommandId" : 16911,
                            "items" : [
                                    {
                                            "spec" : "0.17g*60片/盒",
                                            "productId" : 5004,
                                            "skuId" : 22729,
                                            "productName" : "方盛 血塞通分散片  60片*0.17g/片",
                                            "quantity" : 1,
                                            "usage" : "一天3次,一次2片,饭后服用,口服",
                                            "bakup" : "",
                                            "commonName" : "血塞通分散片"
                                    }
                            ]
                    }
            },
            "containRecom" : 1,
            "containVideo" : 0,
            "sessionId" : "16664_73752_1448348944355",
            "beginTime" : 1448348944355,
            "payType" : 0})


# if __name__ == "__main__":
#     i = 0
#     for i in xrange(300):
#         insert_data()
#         print i
#
