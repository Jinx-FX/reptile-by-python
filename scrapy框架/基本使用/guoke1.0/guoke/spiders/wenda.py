import scrapy
from ..items import GuokeItem

# 果壳问答已gg，这个网站是失效的，看看语法就行

class WendaSpider(scrapy.Spider):
    name = 'wenda'
    allowed_domains = ['guokr.com']  # 允许的域
    start_urls = ['https://www.guokr.com/ask/highlight/?page=0']  # 起始的url   

    def parse(self, response):
        """不能修改方法名称,这个方法是用来解析start_urls的响应"""
        # res = response.xpath("//ul[@class='ask-list-cp']/li/div[2]/h2/a/text()").extract()  # 提取满足xpath的所有结果
        # res = response.xpath("//ul[@class='ask-list-cp']/li/div[2]/h2/a/text()").extract_first()  # 提取满足xpath的第一个结果
        # res = response.xpath("//ul[@class='ask-list-cp']/li/div[2]/h2/a/text()").get()  # 提取满足xpath的第一个结果
        # res = response.xpath("//ul[@class='ask-list-cp']/li/div[2]/h2/a/text()").getall()  # 提取满足xpath的所有结果
        # #  使用xpath获取到的是列表对象，使用get可以获取到列表的的一个元素，getall可以获取列表的所有元素
        # #  这里的xpath和etree中的xpath没有关系，这里是response对象所具有的方法
        # for i in res:
        #     print(i)
        nodes = response.xpath("//ul[@class='ask-list-cp']/li/div[2]/h2/a")
        #  找到的是网页中对应20个问题的a节点
        for node in nodes:
            question = node.xpath('./text()').get()
            # print(question)
            # dict_data = {}
            item = GuokeItem()
            #  把item当成字典来使用和理解
            #  注意：字典的key一定要跟items文件中定义的相对应
            item['question'] = question
            # print(item)
            yield item  # 构造完item以后，使用yield传递给引擎，然后给管道