# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DiseasespiderPipeline(object):
    def process_item(self, item, spider):
        with open('ill_file.txt', 'a+') as f:
            text = str(item['symptom_name']) + '\n' + str(item['symptom_link']) + '\n' + str(item['disease_name'])+ '\n' +'*'*40+ '\n'
            f.write(text)
        return item