# -*- coding: utf-8 -*-
import scrapy
from ..items import DongguanItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=2']

    def parse(self, response):
        """解析start_urls的响应"""
        nodes = response.xpath("//li[@class='clear']")  # 问题共同的节点列表
        for node in nodes:
            print(response.request.headers)
            item = DongguanItem()
            item['status'] = node.xpath("./span[2]/text()").get().strip()
            item['title'] = node.xpath("./span[3]/a/text()").get()
            detail_url = response.urljoin(node.xpath("./span[3]/a/@href").get())
            #可以添加headers参数
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={"item": item}) 
            # print(detail_url)
        next_url = response.xpath("//a[@class='arrow-page prov_rota']/@href").get()  #下一页

        yield response.follow(next_url, callback=self.parse)   #递归

    def parse_detail(self, response):
        print(response.request.headers)
        item = response.meta.get("item")
        item['publish_time'] = response.xpath("//span[contains(text(),'发布日期')]/text()").get()[4:]
        ques_content = '这个问题没有内容'
        try:
            ques_content = response.xpath("//pre")[0].xpath('./text()').get()
        except:
            pass
        item['ques_content'] = ques_content

        answer = "这个问题暂时还没有回复"
        try:
            answer = response.xpath("//pre")[1].xpath('./text()').get()
        except:
            pass
        item['answer'] = answer
        yield item
        # print(item)
