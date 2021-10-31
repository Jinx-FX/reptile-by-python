# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MeizituItem


class MeinvSpider(CrawlSpider):
    name = 'meinv'
    allowed_domains = ['tupianzj.com'] #这里不要写斜杆  如果终端右offsite输出，一般是这里错了
    start_urls = ['https://www.tupianzj.com/meinv/mm/meizitu/']

    rules = (
        Rule(LinkExtractor(allow=r'/meinv/\d+/\d+\.html')
            , callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = MeizituItem()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        pic_url = response.xpath("//div[@id='bigpic']/a[2]/img/@src").get()
        name = response.xpath("//div[@class='list_con bgff']/h1/text()").get()
        print(pic_url)
        item['image_urls'] = [pic_url]
        item['name'] = name
        return item
