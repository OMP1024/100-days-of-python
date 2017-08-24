# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib2
import cookielib

cookiejar = cookielib.MozillaCookieJar()

cookiejar.load('cookie.txt')

handler = urllib2.HTTPCookieProcessor(cookiejar)

opener = urllib2.build_opener(handler)

response = opener.open("http://www.baidu.com")

print response.read()
