# -*- coding:utf-8 - *-

import requests
from lxml import  etree
from queue
import threading
import time
import json

class thread_crawl(threading.Thread):
    """
    抓取线程
    """

    def __init__(self,threadID,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q

    def run(self):
        print('starting' + self.threadID)
        self.qiushi_spider()
        print('exiting',self.threadID)

    def qiushi_spider(self):

        while True:

            if self.q.empty():
                break
            else:
                page = self.q.get()
                print('qiushi_spider = ',self.threadID,'Page = ',str(page))
                url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                    'Accept-Language': 'zh-CN,zh;q=0.8'}
                timeout =4
                while timeout > 0:
                    timeout -= 1
                    try:
                        content = requests.get(url,headers=headers)
                        data_queue.put(content.text)
                        break
                    except Exception as e:
                        print(e)

                if timeout < 0:
                    print('timeout',url)


class Thread_Parse(threading.Thread):

    """
    页面解析
    """

    def __init__(self,threadID,queue,lock,f):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.queue = queue
        self.f = f

    def run(self):
        print('starting',self.threadID)

        global total,exitFlag_Parser
        while not exitFlag_Parser:
            try:
                """
                调用队列对象的 get()方法从队头删除并返回一个项目，可选参数为 block 默认为 True
                如果队列为空且 block为 True，get()就调用线程暂停，直至有项目可用。
                如果队列为空且 block 为 False，队列将引发 empty 异常
                """
                item = self.queue.get(False)
                if not item:
                    pass
                self.parse_data(item)