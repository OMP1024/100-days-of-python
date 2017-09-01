# -*- coding: utf-8 -*-
__author__ = 'abbot'


from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import json

def tencent():
    url = 'http://hr.tencent.com/'
    req = request.Request(url + 'position.php?&start=10#a')
    response = request.urlopen(req)
    resHtml = response.read()

    output = open('tencent.json','w')
    html = BeautifulSoup(resHtml,'lxml')

    result = html.select('tr[class="even"]')
    result2 = html.select('tr[class="odd"]')

    result += result2

    items = []

    for site in result:
        item = {}

        name = site.select('td a')[0].get_text()
        detailLink = site.select('td a')[0].attrs['href']
        catalog = site.select('td')[1].get_text()
        recruitNumber = site.select('td')[2].get_text()
        workLocation = site.select('td')[3].get_text()
        publishTime = site.select('td')[4].get_text()

        item['name'] = name
        item['detailLink'] = url + detailLink
        item['catalog'] = catalog
        item['recruitNumber'] = recruitNumber
        item['publishTime'] = publishTime

        items.append(item)

    line = json.dumps(items,ensure_ascii=False)

    output.write(line)
    output.close()


if __name__ == '__main__':
    tencent()
