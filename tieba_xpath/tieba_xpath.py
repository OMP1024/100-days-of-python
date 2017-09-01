# -*- coding: utf-8 -*-
__author__ = 'abbot'

import os
import urllib
from lxml import etree
from urllib import parse
from urllib import request
import ssl


class Spider:

    def __init__(self):

        self.tiebaName = input("请输入要访问的贴吧：")
        self.beginPage = int(input("请输入起始页："))
        self.endPage = int(input("请输入终止页："))

        self.url = 'http://tieba.baidu.com/f'
        self.ua_headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

        # 忽略未经审核的SSL证书认证
        self.context = ssl._create_unverified_context()

        # 图片编号
        self.userName = 1


    def tiebaSpider(self):

        for page in range(self.beginPage,self.endPage+1):
            pn = (page- 1) * 50
            word = {'pn': pn,'kw':self.tiebaName}

            word = parse.urlencode(word)
            myUrl = self.url + '?' + word

            print(myUrl)

            self.loadPage(myUrl)


    def loadPage(self,url):
        req = request.Request(url,headers=self.ua_headers)
        html = request.urlopen(req,context=self.context).read()

        selector = etree.HTML(html)

        imagesLinks = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for link in imagesLinks:
            link = 'http://tieba.baidu.com' + link
            print(link)
            self.loadImage(link)


    def loadImage(self,url):
        req = request.Request(url,headers=self.ua_headers)
        html = request.urlopen(req,context=self.context).read()

        selector = etree.HTML(html)

        print(selector)

        imageslinks = selector.xpath('//img[@class="BDE_Image"]/@src')

        for link in imageslinks:
            print(imageslinks)
            self.writeImages(link)


    def writeImages(self,imagesLink):
        print(imagesLink)
        images = request.urlopen(imagesLink,context=self.context).read()

        with open('./images/'+str(self.userName) + '.png','wb') as f:
            f.write(images)

        self.userName += 1


if __name__ == '__main__':

    mySpider = Spider()
    mySpider.tiebaSpider()

