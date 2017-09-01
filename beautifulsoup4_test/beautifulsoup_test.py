# -*- coding: utf-8 -*-
__author__ = 'abbot'


from bs4 import BeautifulSoup
import lxml
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建一个Beautiful Soup 对象,并制定解释器 lxml
soup = BeautifulSoup(html,'lxml')

# 打开本地 HTML 文件的方式传感对象，指定解释器 lxml
soup1 = BeautifulSoup(open('index.html'),'lxml')

# 输出格式化soup内容
print(soup.prettify())

# 输出tag
print(soup.title)

print(soup.p)

print(soup.head)

# 输出tag的类型
print(type(soup.p))

# 输出tag的属性
print(soup.p.attrs)

print(soup.head.name)

print(soup.p['class'])

soup.p['class'] = 'newClass'

print(soup.p.attrs)

del soup.p['class']

print(soup.p.attrs)

print(soup.a.string)

soup.a.string = '哈哈哈'

print(soup.a)

print(soup.a.string)

print(soup.head.children)

for child in soup.body.children:
    print(child)


print(soup.find_all('a'))


for tag in soup.find_all(re.compile('^b')):
    print(tag.name)


for tag in soup.find_all(['a','p']):
    print(tag.name)


print(soup.find_all(id = 'link1')[0].string)

# CSS选择器，通过标签名查找
print(soup.select('title'))

print(soup.select('a'))

print(soup.select('b'))


# 通过类名查找
print(soup.select('.sister'))


# 通过id查找
print(soup.select('#link1'))


# 组合查找
print(soup.select('p #link1'))

# 属性查找
print(soup.select('a[class="sister"]'))

for title in soup.select('a[class="sister"]'):
    print(title.get_text())