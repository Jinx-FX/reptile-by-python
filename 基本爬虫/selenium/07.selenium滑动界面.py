from selenium.webdriver import Chrome
import time

driver = Chrome()

url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=78000241_12_hao_pg&wd=selenium%20js%E6%BB%91%E5%8A%A8&fenlei=256&rsv_pq=8215ec3a00127601&rsv_t=a763fm%2F7SHtPeSVYKeWnxKwKBisdp%2FBe8pVsIapxTsrlUnas7%2F7Hoo6FnDp6WsslfyiRc3iKxP2s&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=31&rsv_sug1=17&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=9266&rsv_sug4=9770"

driver.get(url)

js = "document.documentElement.scrollTop=800"  # 滚动到底部
driver.execute_script(js)  # 执行js
time.sleep(1)
js = "document.documentElement.scrollTop=0"  # 滚动到顶部
driver.execute_script(js)  # 执行js

time.sleep(1)
driver.close()
