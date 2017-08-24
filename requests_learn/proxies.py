# -*- coding: utf-8 -*-
__author__ = 'abbot'

import requests
import urllib

# 免费代理
# proxies = {
#   "http": "http://12.34.56.79:9527",
#   "https": "http://12.34.56.79:9527",
# }

# 私密代理
proxy = {"http":"mr_mao_hacker:sffqry9r@61.158.163.130:16816"}

response = requests.get("http://www.baidu.com",proxies = proxy)

print(response.status_code)

print(response.text)

print(response.json())
