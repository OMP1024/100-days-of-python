# -*- coding: utf-8 -*-
__author__ = 'abbot'

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/Users/wangbo/Downloads/phantomjs-2.1.1-macosx/bin')

js = "var q = document.getElementById(\"kw\"); q.style.border=\"2px solid red\";"

driver.execute_script(js)

driver.save_screenshot("redbaid.png")

img = driver.find_element_by_xpath("//*[@id=''lg]/img")
driver.execute_script('$(argument[0]).fadeOut()',img)

driver.execute_script("$")