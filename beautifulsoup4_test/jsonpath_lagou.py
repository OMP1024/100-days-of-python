# -*- coding: utf-8 -*-
__author__ = 'abbot'

from urllib import request
import json
import jsonpath
import ssl

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
context = ssl._create_unverified_context()

req = request.Request(url)
response = request.urlopen(req,context=context)

html = response.read()

print(html)

jsonObj = json.loads(html)

citylist = jsonpath.jsonpath(jsonObj,'$..name')

print(citylist)

print(type(citylist))

fp = open('city.json','w')
content = json.dumps(citylist,ensure_ascii=False)
print(content)

fp.write(content)
fp.close()

