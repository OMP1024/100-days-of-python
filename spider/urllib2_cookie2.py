# -*- coding: utf-8 -*-
__author__ = 'abbot'

"""
获取网站cookie并保存到本地文件中
"""

import urllib2
import cookielib

# 文件名
filename = "cookie.txt"

cookiejar = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookiejar)

opener = urllib2.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookiejar.save()


