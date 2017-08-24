# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

header = {"User-Agent": "Mozilla...."}

formdata = {
    'start':'0',
    'limit':'10'
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url,data=data,headers=header)

response = urllib2.urlopen(request)

print response.read()

