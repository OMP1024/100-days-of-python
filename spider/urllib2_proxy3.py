# -*- coding: utf-8 -*-
__author__ = 'abbot'

"""
私密代理
"""

import urllib2
import urllib

# 私密代理用户
user = "mr_mao_hacker"

# 私密代理密码
password = "sffqry9r"

# 私密代理IP
proxyserver = "61.158.163.130:16816"

# 构建一个密码管理对象，用来保存需要处理的用户名和密码
passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加代理ip，用户名，密码
passwdmgr.add_password(None,proxyserver,user,password)

# 构建一个代理基础用户名/密码验证的处理器对象
proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)

# 构建一个opener
opener = urllib2.build_opener(proxyauth_handler)

# 构建Requset请求对象
request = urllib2.Request("http://www.baidu.com/")

# 6.使用自定义的opener发送请求
response = opener.open(request)

# 7.打印响应
print response.code

print response.read()


