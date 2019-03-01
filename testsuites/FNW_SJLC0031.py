#-*-coding:utf-8-*-
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver=driver.get('https://sns.xiniunet.com/admin/index.htm')

driver.find_element_by_id('account').send_keys('wangshuyuan@30033')
driver.find_element_by_id('password').send_keys('xn30033')
time.sleep(2)

driver.find_element_by_css_selector("div#head ul>li.header-li a.orange-txt").click()

