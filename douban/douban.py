# -*- coding: utf-8 -*-
__author__ = 'abbot'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS(executable_path='/Users/wangbo/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get('https://www.jianshu.com/sign_in#/')


driver.find_element_by_id("session_email_or_mobile_number").send_keys("912248672@qq.com")
driver.find_element_by_id("session_password").send_keys("rjyza091289WC")

driver.find_element_by_xpath("//input[@class='sign-in-button']").click()

time.sleep(3)

driver.save_screenshot('douban.png')

with open('douban.html','w') as f:
    f.write(driver.page_source)

driver.quit()