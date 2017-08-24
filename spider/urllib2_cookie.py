# -*- coding: utf-8 -*-
__author__ = 'abbot'

"""
 获取Cookie，并保存到CookieJar()对象中
"""

import urllib2
import cookielib

# 构建Cookiejar对象实例来保存cookie
cookiejar = cookielib.CookieJar()

# 使用HTTPCookieProcessor()来创建一个cookie处理器对象，参数为cookieJar
handler = urllib2.HTTPCookieProcessor(cookiejar)

# 通过build_opener()来构建一个opener
opener = urllib2.build_opener(handler)

# 以get方式访问页面，访问之后会自动保存cookie到cookiejar中
opener.open("http://www.baidu.com")

# 按标准格式将保存的cookie打印出来
cookiestr = ""
for item in cookiejar:
    cookiestr = cookiestr + item.name + "=" + item.value + ";"

# 去掉最后一位分号
print cookiestr[:-1]






