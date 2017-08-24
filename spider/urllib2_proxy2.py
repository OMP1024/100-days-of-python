# -*- coding: utf-8 -*-
__author__ = 'abbot'


import urllib2
import random

# 免费代理用的人多，不稳定
proxy_list = [
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"}
]

# 随机选择一个代理
proxy = random.choice(proxy_list)

# 使用选中的代理构建代理处理器对象
httpproxy_handler = urllib2.ProxyHandler(proxy)

# 根据处理器对象handler创建opener
opener = urllib2.build_opener(httpproxy_handler)

# 创建一个请求
request = urllib2.Request("http://www.baidu.com/")

# 用构建的opener 打开一个请求
response = opener.open(request)

print response.read()