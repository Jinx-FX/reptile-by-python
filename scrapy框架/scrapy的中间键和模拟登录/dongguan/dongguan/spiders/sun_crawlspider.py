# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunCrawlspiderSpider(CrawlSpider):
    name = 'sun_crawlspider'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=2']

    # rules代表对于提取到的url所构造的 （ 请求 的 规则 ）
    # LinkExtractor代表提取url的规则
    # callback代表提取到的url所构造的请求的响应由谁处理
    #follow 表示进入 url的详情页之后，是否还要按照 rule进行提取，一般不用，即 =false
    rules = (
        # Rule(LinkExtractor(allow=r'正则语句', restrict_xpaths="xpath语句"), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/political/politics/index\?id=\d+')
            , callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
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
        # return item
        print(item)
