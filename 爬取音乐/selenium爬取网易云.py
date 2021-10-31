import time
from selenium import webdriver

# 实例化一个谷歌浏览器出来
dirver = webdriver.Chrome()

url = 'https://music.163.com/#/discover/playlist/'

dirver.get(url)

# 当网页中的数据在iframe或者frame中的时候
# 你可以理解为 数据不再当前页面 而是在iframe框架中
# 进入框架 获取数据
# switch_to.frame()
dirver.switch_to.frame('g_iframe')
# 先获取元素 在获取文本
# title = dirver.find_element_by_xpath('//*[@id="m-pl-container"]/li[11]/p[1]/a').text
# print(title)
# 先定位到元素 再通过get_attribute方法获取数据
# hrefs = dirver.find_elements_by_xpath('//*[@id="m-pl-container"]/li[*]/p[1]/a')
# for href in hrefs:
#     print(href.get_attribute('href'))

# 先获取一部分xpath 再接着用xpath
# //*[@id="m-pl-container"]/li[11]/p[1]/a
# //*[@id="m-pl-container"]/li[11]/p[2]/a
for i in range(5): # 01234
    nodes = dirver.find_elements_by_xpath('//*[@id="m-pl-container"]/li')  # 获取全部的li元素

    for node in nodes:
        # node 是上面li元素的每一个  text 获取文本  get_attribute 获取属性
        title = node.find_element_by_xpath('./p[1]/a').text
        name = node.find_element_by_xpath('./p[2]/a').get_attribute('title')
        print('title:',title,'\t\tname:',name)
    time.sleep(2)

    # 当我们用xpath获取不到元素点击的时候 或者找不到的时候 可以使用前端的点击
    # dirver.find_element_by_xpath('//*[@id="m-pl-pager"]/div/a[11]').click()
    # arguments[0].click() 点击事件
    next_node = dirver.find_element_by_xpath('//*[@id="m-pl-pager"]/div/a[11]')
    dirver.execute_script('arguments[0].click()',next_node) # 前端的点击事件
    # 保存数据 {name:title}  {name:'',titile:''}

    # #  找到下一页的a节点，模拟点击
    # next_node = webdriver.find_element_by_link_text('下一页')
    # next_node.click()

    # #  翻页有两种方法：1.找url的规律，修改url
    # #                2.模拟点击下一页
dirver.close()