import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BqgtextItem

class Bqg2Spider(CrawlSpider):
    name = 'bqg2'
    allowed_domains = ['xbiquge.la']
    start_urls = ['https://www.xbiquge.la/8/8102/']

    # LinkExtractor(allow=r'Items/') 链接提取器 提取链接  请求的就是提取链接的url
    # callback='parse_item' 回调函数
    # follow = True  可以将提取的链接 可以继续在方面里面使用
    link = LinkExtractor(allow=r'/8/8102/\d+.html') # \d 数字
    # 凡是获取到链接的都请求一次
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.request.url)
        item = BqgtextItem()
        item['title'] = response.xpath('/html/head/meta[4]/@content').get()
        item['data'] = response.xpath('//*[@id="content"]/text()').getall()
        print(item)
        return item
