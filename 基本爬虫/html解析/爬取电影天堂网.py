import requests
import json
from lxml import etree
from urllib.parse import urljoin

# 确定url
url = "https://www.dytt8.net/html/gndy/dyzz/index.html"

# 先发送请求，确认响应的内容是否完整
response = requests.get(url)
text = response.content.decode('gbk', errors='ignore')#有一乱码无法输出，选择忽视
# print(text)

# 把响应文本转换成html
html = etree.HTML(text)

#  找到列表页中所有的a节点
nodes = html.xpath('//a[@class="ulink"]')

#  遍历a节点，构造字典 用来保存数据
for node in nodes:
    dict_data = {}
    dict_data['movie_name'] = ''.join(node.xpath('./text()'))
    detail_url = ''.join(node.xpath('./@href'))
    # 手动拼接url
    # detail_url = "https://www.dytt8.net" + detail_url
    # 利用urllib里的方法拼接
    detail_url = urljoin(response.url, detail_url)
    # print(detail_url)
    # print(response.url)
    # print(detail_url)
    # print(requests.get(detail_url).content.decode('gbk', errors='ignore'))
    detail_text = requests.get(detail_url).content.decode('gbk', errors='ignore')
    detail_html = etree.HTML(detail_text)
    download_url = ''.join(detail_html.xpath("//a[starts-with(@href,'magnet')]/@href"))
    dict_data['download_url'] = download_url
    print(dict_data)

# xpath中starts-with(text(),'str')  寻找text文本是以str开头这样的节点
# xpath中starts-with(@href,'str')  寻找href属性是以str开头这样的节点
# //font[contains(text(),'磁力链点击')]/ancestor::font/ancestor::font/ancestor::strong/ancestor::a/@href
# //a[starts-with(@href,'magnet')]/preceding-sibling::img # 向上找img兄弟节点
# //a[starts-with(@href,'magnet')]/following-sibling::img # 向下找img兄弟节点
