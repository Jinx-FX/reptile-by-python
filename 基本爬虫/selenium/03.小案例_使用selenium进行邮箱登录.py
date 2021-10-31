import time
from selenium import webdriver

# 实例化一个谷歌浏览器出来
driver = webdriver.Chrome()
url = 'https://mail.sina.com.cn/'
driver.get(url)

# 定位到指定元素  写入账号
driver.find_element_by_xpath('//*[@id="freename"]').send_keys('q1069916147@sina.com')
# 写入密码
driver.find_element_by_id('freepassword').send_keys(input('请输入你的密码:'))
# 点击登录
driver.find_element_by_link_text('登录').click()
time.sleep(4)
# 退出
driver.close()