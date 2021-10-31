# 等待页面加载完成 : 隐示等待
# 等待元素加载完成： 显示等待  需要一个元素
# 就是要等待         time
# import time
# time.sleep(2)

# from selenium import webdriver
#
# url = 'https://fanyi.baidu.com/translate?'
# driver = webdriver.Chrome()
# # 使用隐示等待 等待10秒钟 页面加载完成 如果提前加载完成 就会往后执行不需要等待10秒钟
# driver.implicitly_wait(10)
# driver.get(url)
# driver.implicitly_wait(10)
# driver.close()
# print('页面执行完了')

# 显示等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.baidu.com'
driver = webdriver.Chrome() 
driver.get(url)

# 定位元素 设置等待时间
# 第一个参数 上面实例化的浏览器
# 第二个参数 等待5秒钟
# 第三个参数 0.5秒钟检测一次
# WebDriverWait 要和until 搭配使用  until写定位的元素
# 1.获取元素 2.等待和检测元素啥时候加载完成
node = WebDriverWait(driver,1,0.1).until(EC.presence_of_element_located((By.ID,'kw')))
node.send_keys('六星教育')