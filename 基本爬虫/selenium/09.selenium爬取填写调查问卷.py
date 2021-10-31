#  selenium 的作用：模拟浏览器
#  优点：不需要考虑反爬，因为完全模拟浏览器工作
#  为什么需要用无头模式： 使用selenium来做爬虫 
# 不需要页面，也需要网页的源代码就可以了，采用无头模式，
# 省去了页面渲染，可以提升效率

from selenium.webdriver import Chrome
import random

#  找url
url = "https://www.wjx.cn/jq/37766520.aspx" #调查问卷

#  实例化一个浏览器对象
webdriver = Chrome()

#  使用webdriver访问目标网站
webdriver.get(url)

#  解析网页结构  若右键打不开，，可以用F12打开，笔记本（Fn+F12）

#  找到网页中文本为男的label节点，再找同级的a节点，然后再点击
ele = webdriver.find_element_by_xpath("//label[text()='男']/preceding-sibling::a")
ele.click()
#  找到网页中文本为艺体的label节点，再找同级的a节点，然后再点击
ele = webdriver.find_element_by_xpath("//label[text()='艺体']/preceding-sibling::a")
ele.click()
#  找到网页中文本为大一的label节点，再找同级的a节点，然后再点击
ele = webdriver.find_element_by_xpath("//label[text()='大一']/preceding-sibling::a")
ele.click()

# eles = webdriver.find_elements_by_xpath("//label[text()='非常符合']/preceding-sibling::a")
# for ele in eles:
#     ele.click()

# 找到所有问题的ul节点（切掉前三个特殊的问题）
eles = webdriver.find_elements_by_xpath("//ul[@class='ulradiocheck']")[3:]

for ele in eles:
    num = random.randint(1, 4)
    a_ele = ele.find_element_by_xpath("./li[{}]/a".format(num))
    a_ele.click()
    # 找到每个选项下的label节点，获取label节点的文本和属性
    label_ele = ele.find_element_by_xpath("./li[{}]/label".format(num))
    # selenium方法里面无text的写法，只能找节点
    # 提取标签的文本和for节点的值
    print(label_ele.text, label_ele.get_attribute("for"))

#  找到提交按钮，点击提交 id="submit_button"
# ele = webdriver.find_element_by_id("submit_button")
# ele.click()
