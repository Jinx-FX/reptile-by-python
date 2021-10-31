import requests
from lxml import etree
import json

with open('wenda.json', 'w', encoding='utf-8')as f:
    # 确定url,列表页的url
    url = "https://www.guokr.com/ask/highlight/?page=1"  #这个网址没了
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
            }

    # 发送请求，获取列表页响应
    response = requests.get(url, headers=headers)
    # print(response.text) # 验证响应的正确性
    #  把响应文本做格式化
    html = etree.HTML(response.text)
    # 找到25个问题对应的a节点列表
    nodes = html.xpath("//div[@class='ask-list-detials']/h2/a")
    for node in nodes:
        dict_data = {}
        dict_data['question'] = ''.join(node.xpath("./text()"))
        detail_url = ''.join(node.xpath("./@href"))  # 获取每个问题的详情页url
        # print(detail_url)
        # print(dict_data)
        # 向详情页url发送请求
        detail_response = requests.get(detail_url, headers=headers)
        # 给详情页的响应文本做格式化
        detail_html = etree.HTML(detail_response.text)
        #  两种方法都可以从详情页的响应中提取出最佳答案
        # answer = ''.join(detail_html.xpath("//div[@class='answer-txt answerTxt gbbcode-content'][1]//p/text()"))
        answer = detail_html.xpath("string(//div[@class='answer-txt answerTxt gbbcode-content'][1])")
        # print(answer)
        # 提取出answer以后，添加到字典中
        dict_data['answer'] = answer
        print(dict_data)
        # 将字典转成字符串然后写入文件
        f.write(json.dumps(dict_data, ensure_ascii=False) + ',\n')