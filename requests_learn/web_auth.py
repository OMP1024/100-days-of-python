
# -*- coding: utf-8 -*-
__author__ = 'abbot'

import requests

auth = ('test','123456')

response = requests.get('http://192.168.199.107',auth = auth)

print(response.text)