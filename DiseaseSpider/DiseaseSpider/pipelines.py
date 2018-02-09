# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo


class DiseasespiderPipeline(object):
    # 写内容到文件
    def process_item(self, item, spider):
        with open('ill_file.txt', 'a+') as f:
            text = str(item['symptom_name']) + '\n' + str(item['symptom_link']) + '\n' + str(item['disease_name']) \
                   + '\n' + str(item['disease_desc']) + '\n'+'*'*100 + '\n'
            f.write(text)
        return item

    # # 写内容到mongodb
    # def __init__(self):
    #     port = settings['MONGODB_PORT']
    #     host = settings['MONGODB_HOST']
    #     db_name = settings['MONGODB_DBNAME']
    #     client = pymongo.MongoClient(host=host, port=port)
    #     db = client[db_name]
    #     self.post = db[settings['MONGODB_DOCNAME']]
    #
    # def process_item(self, item, spider):
    #     symptom_info = dict(item)
    #     self.post.insert(symptom_info)
    #     return item