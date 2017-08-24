# -*- coding: utf-8 -*-
__author__ = 'abbot'

"""
    代理IP是爬虫的第二大招
"""

import urllib2

# 构建两个代理handler ，一个代理有ip，已没有代理ip

httpproxy_handler = urllib2.ProxyHandler({"http" : "121.31.153.187:8123"})
nullproxy_handler = urllib2.ProxyHandler({})

proxySwitch = True

# 构建opener对象
if proxySwitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

request = urllib2.Request("http://www.baidu.com/")

response = opener.open(request)

print response.read()
