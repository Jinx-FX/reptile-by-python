from  selenium import webdriver
from selenium.webdriver import ActionChains
import time
url = 'https://www.helloweba.net/demo/2017/unlock/'
driver = webdriver.Chrome()
driver.get(url)
# 获取到滑块
button = driver.find_element_by_class_name('slide-to-unlock-handle')
# 实例化 ActionChains 对象
action = ActionChains(driver)
# 点击鼠标左键 不松开
action.click_and_hold(button).perform()
# action.move_by_offset(260,0).perform()
action.drag_and_drop_by_offset(button,260,0)
time.sleep(2)
# 清空ActionChains

action.reset_actions()
