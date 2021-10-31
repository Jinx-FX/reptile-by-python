# 可以参考selenium_python的中文文档

from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options

# selenium的特点：效率低，但是不用考虑请求和响应的细节，能够忽视掉很多反爬细节

# 开启无头模式：在创建浏览器对象之前，创建option对象

# 无头浏览似乎是一个奇怪的术语，
# 但它只是一个没有可识别的图形界面的浏览器或浏览器模拟的名称。
# 与使用熟悉的图形元素测试站点或执行常见操作不同，
# 用例是自动化的，并使用命令行界面进行测试。

# option = Options()  # 实例化option对象
# option.add_argument("headless")  # 给option对象添加无头参数

driver = Chrome()

# 若找不到chrome binary 
# 见 解决方法：
# 找到selenium源码 用户AppData ....
# 找到options.py    把自己的chrome文件位置放在_binary_location变量中  ，问题成功解决。

# driver = Chrome(r"C:/Program Files/Python38/chromedriver.exe")
# driver = Chrome(executable_path=r"E:\chromedriver.exe",  
                # 实例化浏览器对象,可以指定chromedriver的路径,
                # 不指定的话 默认会去找python解释器的同级目录
                # options=option
                # 实例化浏览器对象的时候 把option对象带进来
                # )
driver.get("https://www.baidu.com/")

# driver.save_screenshot('baidu.jpg')  # 保存当前网页的截图
# driver.close()  # 关闭当前网页

driver.maximize_window()  # 浏览器窗口最大化

ele = driver.find_element_by_id("wd")  # 找到id为kw的节点  是html的节点
ele.send_keys("数学")  # 向input输入框输入数据

ele = driver.find_element_by_id('su')  # 找到id为su的节点  是html的节点
ele.click()  # 模拟点击

# # 找到文本值为百度一下的节点
# driver.find_element_by_link_text("百度一下")  
# # 根据链接包含的文本获取元素列表，模糊匹配
# driver.find_elements_by_partial_link_text("度一下")  

# ele.text # 获取当前节点的文本
# ele.get_attribute("data-click")  # 获取到属性对应的value

# find_element  找到满足条件的第一个节点
# find_elements  找到所有满足条件的节点

print(driver.page_source)  # 打印网页的源码
print('----')
print(driver.get_cookies())  # 打印出网页的cookie
print('----')
print(driver.current_url)  # 打印出当前网页的url

# time.sleep(3)
# driver.quit()  # 直接关闭浏览器
