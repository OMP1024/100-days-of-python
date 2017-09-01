# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShangqiuItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 分类
    category = scrapy.Field()
    # 位置
    location = scrapy.Field()
    # 开发商
    developer = scrapy.Field()
    # 单价
    price = scrapy.Field()
    # 详情的url
    infoUrl = scrapy.Field()
