# requests + xpath  === > response
# selenium + xpath ====> elements
# respone 和 elements 内容可能是一样的
# 在下载插件的时候 找一个相近的版本就可以了
# 记得添加path
# 注意：版本一定要是相近的版本 不然可能兼容不了
import time
from selenium import webdriver

# 实例化一个谷歌浏览器出来
dirver = webdriver.Chrome()

# 打开一个页面
url = "https://www.sixstaredu.com/"
dirver.get(url)

# dirver.save_screenshot('六星.png')
print(dirver.title)
# time.sleep(1)
# 运行完了关闭页面
# dirver.close()