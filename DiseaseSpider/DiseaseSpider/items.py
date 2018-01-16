# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiseasespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symptom_name = scrapy.Field()
    symptom_link = scrapy.Field()
    disease_name = scrapy.Field()
    # disease_desc = scrapy.Field()
