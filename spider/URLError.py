# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib2

# request = urllib2.Request("http://www.dsajlkf.com")
#
# try:
#     urllib2.urlopen(request,timeout=5)
# except urllib2.URLError,err:
#     print err
#

request = urllib2.Request("http://blog.baidu.com/itcast")

try:
    urllib2.urlopen(request)

except urllib2.HTTPError,err:
    print err.code

except urllib2.URLError,err:
    print err

else:
    print 'good job'