import scrapy


class Bqg3Spider(scrapy.Spider):
    name = 'bqg3'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
