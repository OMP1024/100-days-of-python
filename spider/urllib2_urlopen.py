# -*- coding: utf-8 -*-
__author__ = 'abbot'


import urllib2

url = "http://www.baidu.com"

request = urllib2.Request(url)

response = urllib2.urlopen(request)

print response.read()

