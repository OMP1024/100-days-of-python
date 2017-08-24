# -*- coding: utf-8 -*-
__author__ = 'abbot'

import requests

# response = requests.get("https://www.12306.cn/mormhweb/", verify = False)
# print(response.text)

response = requests.get("http://www.baidu.com")

print(response.content)
