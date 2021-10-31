# -*- coding: utf-8 -*-
import scrapy
from ..items import GuokeItem
from urllib.parse import urljoin
from copy import deepcopy


class WendaSpider(scrapy.Spider):
    name = 'wenda'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/?page=0']

    def parse(self, response):
        nodes = response.xpath("//div[@class='ask-list-detials']/h2/a")
        for node in nodes:
            question = node.xpath('./text()').get()
            #  找到详情页的url
            detail_url = node.xpath('./@href').get()
            item = GuokeItem()
            item['question'] = question
            # 在for循环里面发送详情页的请求
            #  构造详情页的Requests对象，发送给调度器
            #  callback代表响应由哪个方法来处理
            #  meta代表参数传递
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': deepcopy(item)})
            # yield scrapy.Request(detail_url, callback=self.parse_detail)
            # yield item
        next_url = response.xpath("//a[text()='下一页']/@href").get()
        # next_url = response.urljoin(next_url)
        # yield scrapy.Request(next_url, callback=self.parse)
        yield response.follow(next_url, callback=self.parse)

    def parse_detail(self, response):
        """处理一个对应的详情页响应"""
        item = response.meta.get('item')
        # print(item)
        # item = GuokeItem()
        answer = ''.join(response.xpath("//div[@class='answer-r']")[0].xpath('./div[3]//p/text()').getall())
        # question = response.xpath("//h1[@id='articleTitle']/text()").get()
        # print(answer)
        item['answer'] = answer
        # item['question'] = question
        print(item)
        yield item
