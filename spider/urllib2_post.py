# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib
import urllib2

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

header = {"User-Agent": "Mozilla...."}

kw = raw_input("输入要翻译的英文单词：")

formdata = {
    "type":"AUTO",
    "i":kw,
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url,data=data,headers=header)

response = urllib2.urlopen(request)

print response.read()

