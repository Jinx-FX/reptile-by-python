import scrapy
from ..items import BqgtextItem

class BqgSpider(scrapy.Spider):
    name = 'bqg'
    allowed_domains = ['xbiquge.la']
    start_urls = ['https://www.xbiquge.la/8/8102/']

    def parse(self, response):
        hrefs = response.xpath('//*[@id="list"]/dl/dd[*]/a/@href').getall()
        titles = response.xpath('//*[@id="list"]/dl/dd[*]/a/text()').getall()

        for i in range(len(hrefs)):
            item = BqgtextItem()
            item['title'] = titles[i]
            url = 'https://www.xbiquge.la'+ hrefs[i]
            # print(url)
            yield scrapy.Request(url,callback=self.detail_parse,meta={'item':item})
            # yield response.follow() # 自动拼接url 自己带前缀
    def detail_parse(self,response):
        item = response.meta.get('item')
        data = response.xpath('//*[@id="content"]/text()').getall()
        item['data'] = data
        # print(data)
        print(item)
        yield item
