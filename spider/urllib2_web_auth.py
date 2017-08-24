# -*- coding: utf-8 -*-
__author__ = 'abbot'


"""
Web客户端授权验证
"""

import urllib2
import urllib

# 用户名
user = "test"

# 密码
passwd = "123456"

# Web服务器 IP
webserver = "http://192.168.199.107"

# 1.构建一个密码管理对象
passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 2.添加账户信息
passwdmgr.add_password(None,webserver,user,passwd)

# 3.构建一个HTTP处理器对象
httpauth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

# 4.通过handler对象构建一个opener对象
opener = urllib2.build_opener(httpauth_handler)

# 5.安装opener为全局的opener对象
urllib2.install_opener(opener)

# 6.构建一个Request对象
request = urllib2.Request(webserver)

# 7.定义opener为全局的opener后，可直接使用urlopen()发送请求
response = urllib2.urlopen(request)

# 打印响应的内容
print response.read()

