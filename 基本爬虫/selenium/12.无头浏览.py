import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 实例化一个对象
options = webdriver.ChromeOptions()
options.add_argument('headless')  # 给对象添加数据  无头浏览 更加节约cpu开销 
# 实例化一个谷歌浏览器出来
dirver = webdriver.Chrome(options=options)

# 打开一个页面
url = "https://www.sixstaredu.com/"
dirver.get(url)

dirver.save_screenshot('六星.png')
print(dirver.title)
time.sleep(1)
# 运行完了关闭页面
dirver.close()