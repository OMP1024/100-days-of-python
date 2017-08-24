# -*- coding: utf-8 -*-
__author__ = 'abbot'

import requests

response = requests.get("http://www.baidu.com")

cookiejar = response.cookies

cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print(cookiejar)

print(cookiedict)

