import requests
from lxml import etree
import json

class Guoke(object):
    def __init__(self):
        #  请求的url
        self.url = "https://www.guokr.com/ask/highlight/?page=1"
        #  请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        #  打开文件的对象
        self.file = open('wenda.json', 'w', encoding='utf-8')

    def get_response(self, url):
        """发送请求，获取响应,返回响应的文本"""
        response = requests.get(url, headers=self.headers)
        return response.text

    @staticmethod
    def str_to_html(text):
        """把响应的文本转成html对象，返回html对象"""
        html = etree.HTML(text)
        return html

    @staticmethod
    def parse_list(list_html):
        """解析列表页,返回每个a节点对应的问题和详情页url"""
        nodes = list_html.xpath("//div[@class='ask-list-detials']/h2/a")
        print(nodes)
        for node in nodes:
            question = ''.join(node.xpath("./text()"))
            detail_url = ''.join(node.xpath("./@href"))
            yield question, detail_url

    @staticmethod
    def parse_detail(detail_html):
        """解析详情页,传入详情页的html，返回answer"""
        answer = ''.join(detail_html.xpath("//div[@class='answer-txt answerTxt gbbcode-content']//p/text()"))
        # 拿到详情页的高赞答案
        return answer

    @staticmethod
    def save(file, dict_data):
        """保存文件,传入一个字典，把字典的数据保存到文本中"""
        # with open('wenda.json', 'w', encoding='utf-8')as f:
        file.write(json.dumps(dict_data, ensure_ascii=False) + ',\n')

    def run(self):
        """程序的整体调度"""
        list_text = self.get_response(self.url)
        list_html = self.str_to_html(list_text)
        for item in self.parse_list(list_html):
            print(item)
            dict_data = {}  # 每次for循环创建一个字典
            dict_data['question'] = item[0]
            detail_url = item[1]
            # print(dict_data)
            # print(detail_url)
            detail_text = self.get_response(detail_url)
            detail_html = self.str_to_html(detail_text)
            answer = self.parse_detail(detail_html)
            dict_data['answer'] = answer
            print(dict_data)
            # self.save(dict_data)
            # 改写save方法，使其一直打开，直到输出全部保存
            self.save(self.file, dict_data)

    def __del__(self):
        self.file.close()


if __name__ == '__main__':
    guoke = Guoke()
    guoke.run()