# -*- coding: utf-8 -*-
__author__ = 'abbot'

import urllib2
import re
from
class Spider:
    """
    内涵段子爬虫
    """

    def loadpage(self):
        """
        :param page: 下载第几页
        :return: 提取想要的数据
        """

        url = "https://ishuo.cn"

        headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0"}

        request = urllib2.Request(url,headers=headers)

        response = urllib2.urlopen(request)

        print(response.read())


    def filter(self,html):
        """
        :param html: 从html中提取想要的段子
        :return:
        """
        pattern = re.compile(r'<li.*?class>')



if __name__ == "__main__":
    """
    内涵段子小爬虫
    """
    print("按下回车键开始")
    raw_input()

    mySpider = Spider()

    mySpider.loadpage()
