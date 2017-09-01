# -*- coding: utf-8 -*-
import scrapy
from shangqiu.items import ShangqiuItem
import re

class SqspiderSpider(scrapy.Spider):
    name = 'sqSpider'
    allowed_domains = ['newhouse.shangqiu.fang.com/']
    start_urls = ['http://newhouse.shangqiu.fang.com/house/s/b91/']

    page = 1

    def parse(self, response):

        for each in response.xpath("//div[@class='sslalone']"):

            item = ShangqiuItem()

            # 名称
            name = each.xpath('./ul[@class="sslainfor"]/li[1]/strong[@class="f14px"]/a/text()').extract()[0]
            # 分类
            category = each.xpath('./ul[@class="sslainfor"]/li[1]/span[@class="sngrey"]/text()').extract()[0]
            # 位置
            location = each.xpath('./ul[@class="sslainfor"]/li[2]/font/text()').extract()[0]
            # 开发商
            developer = each.xpath('./ul[@class="sslainfor"]/li[4]/a/text()').extract()[0]
            # 单价
            price = each.xpath('./ul[@class="sslaright"]/li[1]/span/text()').extract()[0]
            #
            infoUrl = each.xpath('./div[@class="sslaimg"]/a/@href').extract()[0]

            print(name,category,location,developer,price,infoUrl)

            item['infoUrl'] = infoUrl
            item['name'] = name
            item['category'] = category
            item['location'] = location
            item['developer'] = developer
            item['price'] = price

            self.page += 1

            url = 'http://newhouse.shangqiu.fang.com/house/s/b9' + str(self.page) + '/'

            yield scrapy.Request(url,callback=self.parse)
            yield item
