# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib2
import random

url = "http://www.baidu.com"

# header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

# 随机的User-Agent
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]

# request = urllib2.Request(url,headers=header)

user_agent = random.choice(ua_list)

request = urllib2.Request(url)

request.add_header("User-Agent",user_agent)

# 通过add_header 添加header信息
request.add_header("Connection","keep-alive")

# 可以通过 get_header 查看header的信息
print request.get_header("User-agent")
print request.get_header("Connection")

response = urllib2.urlopen(request)

# response.code 查看返回的状态码
print response.code

print response.read()

