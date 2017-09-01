# -*- coding: utf-8 -*-
__author__ = 'abbot'


import unittest
from selenium import webdriver
from bs4 import BeautifulSoup

class douyuSelenium(unittest.TestCase):

    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path='/Users/wangbo/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')


    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")

        while True:

            # 指定解析方式为xml
            soup = BeautifulSoup(self.driver.page_source,'xml')
            # dy-num fr
            titles = soup.find_all('h3',{'class': 'ellipsis'})
            nums = soup.find_all('span',{'class':'dy-num fr'})

            for num,title in zip(nums,titles):
                print(u'观众人数：',num.get_text().strip(),u'房间标题：',title.get_text().strip())

            if self.driver.page_source.find('shark-pager-next') != -1:
                break

            self.driver.find_element_by_class_name('shark-pager-next').click()
            self.driver.fin


    def tearDown(self):
        print('加载完成...')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()