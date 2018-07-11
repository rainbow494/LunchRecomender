# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:itemText
#     pass
class DianpingItem(scrapy.Item):
    titleCSSSelector = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
