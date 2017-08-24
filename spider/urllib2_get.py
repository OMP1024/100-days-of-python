# -*- coding: utf-8 -*-
__author__ = 'abbot'


import urllib2
import urllib

url = "http://www.baidu.com/s"

keyword = raw_input("输入要搜索的关键字:")

word = {"wd":keyword}

word = urllib.urlencode(word)

newurl = url + "?" + word

header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib2.Request(newurl,headers=header)

response = urllib2.urlopen(request)

print response.code

print response.read()



