#https://movie.douban.com/top250

# coding=utf-8
import requests
from lxml import etree
import json

page = 0

with open('movie.json', 'w', encoding='utf-8')as f:
    # for i in range(int(input('请输入要爬取的页数: '))):
    while True:
        #  确定url
        url = "https://movie.douban.com/top250"
        # params = {
        #     "start": i * 25
        # }
        params = {
            "start": page * 25
        }

        # 发送网络请求,判断是否需要添加请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        response = requests.get(url, headers=headers, params=params)

        #  打印出响应的文本,进行搜索调试
        # print(response.text)

        #  进行格式化，输出html对象，使之可以进行xpath解析
        html = etree.HTML(response.text)

        # 使用xpath进行数据解析,传入xpath表达式

        # 第一种方法
        # #  定位到节点以后，在节点后面加上 /text() 代表取节点的文本值
        # xpath() 引号要不一致

        # names = html.xpath("//div[@class='hd']/a/span[1]/text()")  # 通过xpath找到所有的电影名称
        # scores = html.xpath("//span[@class='rating_num']/text()")  # 通过xpath找到所有的电影评分
        # intros = html.xpath("//span[@class='inq']/text()")  # 通过xpath找到所有的电影简介
        # print(names)
        # print(scores)
        # print(intros)
        # # 保证三个列表长度相同，使用zip对应取出每一个元素
        # for item in zip(names, scores, intros):
        #     print(item)

        # 第二种方法
        # 推荐
        #   先找到所有元素共同的父节点，然后遍历父节点，构造字典数据
        # nodes是一个列表
        nodes = html.xpath('//div[@class="info"]')  # 找到共同的父节点，满足条件的节点列表，也就是25部电影的节点列表
        if not nodes:
            break
        # print(nodes)
        #enumerate返回编号和内容（一个元组），start设置开始节点
        for node in enumerate(nodes, start=page * 25 + 1):
            dict_data = {}
            #  遍历以仍然可以条用xpath方法，在原节点的基础上向下解析
            dict_data['id'] = node[0]#设置编号
            dict_data['name'] = (node[1].xpath('./div/a/span[1]/text()'))[0]#这种效果和join一样
            dict_data['score'] = ''.join(node[1].xpath('.//span[@class="rating_num"]/text()'))
            dict_data['intro'] = ''.join(node[1].xpath('.//span[@class="inq"]/text()'))
            print(dict_data)
            f.write(json.dumps(dict_data, ensure_ascii=False) + ',\n')
        page += 1