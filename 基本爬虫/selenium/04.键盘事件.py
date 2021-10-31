from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

driver.find_element_by_name('wd').send_keys('六星教育')
time.sleep(1)
driver.find_element_by_name('wd').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_name('wd').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_name('wd').send_keys('教育')
time.sleep(1)
driver.find_element_by_name('wd').send_keys(Keys.ENTER)
