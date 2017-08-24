# -*- coding: utf-8 -*-
__author__ = 'abbot'

import requests

# 基本的get请求
print(requests.get("http://www.baidu.com/"))

kw = {'wd':'长城'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get("http://www.baidu.com/s?",params=kw,headers=headers)

# 查看响应的内容
print(response.text)

print('-' * 20)

print(response.content)

print('-' * 20)

print(response.url)

print(response.encoding)

print(response.status_code)