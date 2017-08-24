# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib
import urllib2

def tiebaSpider(url,beginpage,endpage):
    """
    :param url: 需要处理的url
    :param beginpage: 爬虫执行的开始页
    :param endpage: 爬虫执行的截止页
    :return: 返回爬取的html
    """

    for page in range(beginpage,endpage):
        pn = (page - 1) * 50

        filename = "第" + str(page) + "页.html"

        fullurl = url + "&pn=" + str(pn)

        print fullurl

    #     loadpage发送请求获取html页面
        html = loadpage(fullurl)

    #     将获取的html页面写入本地磁盘
        writepage(filename,html)

    print "爬虫完成任务"

def loadpage(url):
    """
    :param url: 需要爬取的url地址
    :return: 返回爬取的html页面
    """

    print "正在爬取网页"

    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = urllib2.Request(url,headers=header)

    response = urllib2.urlopen(request)

    return response.read()


def writepage(filename,html):
    """
    :param filename: 要写入的文件名
    :param html: 要写入的内容
    """

    print "正在存储" + filename

    with open(filename,'a+') as f:
        f.write(html)

    print "-" * 20


# 模拟main函数

if __name__ == "__main__":

    kw = raw_input("请输入需要爬取的贴吧：")

    # 输入起始页和终止页
    beginpage = int(raw_input("请输入起始页："))
    endpage = int(raw_input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"

    key = urllib.urlencode({"kw":kw})

    url = url + key + "&ie=utf-8"

    tiebaSpider(url,beginpage,endpage)



