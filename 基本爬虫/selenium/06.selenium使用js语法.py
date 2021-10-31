from selenium.webdriver import Chrome
import time
driver = Chrome()
driver.get('https://www.baidu.com/s?ie=UTF-8&wd=%E5%85%AD%E6%98%9F%E6%95%99%E8%82%B2')

for i in  range(0,3000,50):
    # 用到js代码
    js = 'document.documentElement.scrollTop = %s'%i
    # execute_script 执行js语法
    driver.execute_script(js)

    time.sleep(1)

# selenium 无视大部分的反爬 人可以操作的 一般selenium也可以操作
# selenium可以直接使用打开后的网页
