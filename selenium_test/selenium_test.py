# -*- coding: utf-8 -*-
__author__ = 'abbot'


from selenium import webdriver

from  selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(executable_path='/Users/wangbo/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.get('http://www.baidu.com/')

data = driver.find_element_by_id('wrapper').text

print(data)

print(driver.title)

driver.save_screenshot('baidu.png')

driver.find_element_by_id('kw').send_keys(u'长城')

html = driver.page_source

with open('长城.html','w+') as f:
    f.write(html)

print("source: ",driver.page_source)

print("cookie: ",driver.get_cookies())

print(driver.current_url)

driver.close()

driver.quit()



