import scrapy
import re
import json
import jsonpath

class SixstartextSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'sixstarText'
    # 域(域名 范围) 爬取的链接 不能超出这个域的范围
    allowed_domains = ['sixstaredu.com']
    # 开始的url
    start_urls = ['https://www.sixstaredu.com/teacher']

    def parse(self, response):
        '''用来提取数据'''
        names = response.xpath('//*[@id="content-container"]/div/div[*]/div/div[1]/h3/a/text()').getall()
        # print(names)
        for i in range(20):
            item = {}
            item['name'] = names[i]
            yield item
        # yield在循环外面 先执行上面的循环完 item结果就只有最后一个
        # yield item
