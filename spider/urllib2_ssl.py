# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib2
import urllib
# 1.导入ssl模块
import ssl

def writepage(filename,html):
    """
    写入本地
    :param filename: 文件名字
    :param html: 要写入的内容
    """

    with open(filename,'a+') as f:
        f.write(html)


    print "-" * 20

# 2.忽略未经核实的SSL证书认证
context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"
# url = "http://www.baidu.com"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request = urllib2.Request(url, headers = headers)

# 3.在urlopen()方法里指明添加context参数
response = urllib2.urlopen(request,context=context)

html = response.read()

writepage("铁路.html",html)

print html




