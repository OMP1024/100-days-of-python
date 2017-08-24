# -*- coding: utf-8 -*-
__author__ = 'abbot'

import requests

sission = requests.session()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

sission.post("http://www.renren.com/PLogin.do",data=data,headers=headers)

response = sission.get("http://www.renren.com/PLogin.do")

print(response.json())

with open("renren.html",'a+') as f:
    f.write(response.json())

r = requests.get("https://www.baidu.com/", verify = True)

print(r.text)