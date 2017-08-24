# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib2

url = "http://www.baidu.com"

ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request = urllib2.Request(url,headers=ua_header)

response = urllib2.urlopen(request)

print response.read()

