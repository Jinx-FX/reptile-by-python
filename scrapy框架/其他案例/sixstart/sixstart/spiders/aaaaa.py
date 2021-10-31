import scrapy


class AaaaaSpider(scrapy.Spider):
    name = 'aaaaa'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
