import time
from selenium import webdriver

# 实例化一个谷歌浏览器出来
driver = webdriver.Chrome()

url = 'https://www.baidu.com'
driver.get(url)
# send_keys 往输入框里输入内容
driver.find_element_by_id('kw').send_keys('六星教育')
# 点击事件  click()
driver.find_element_by_id('su').click()
time.sleep(2)
print(driver.page_source)
print(driver.current_url)
time.sleep(3)
# driver.save_screenshot('六星.png')
# 关闭浏览器 节约空间
driver.close()