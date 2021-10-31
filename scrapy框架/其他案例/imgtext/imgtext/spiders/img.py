import scrapy
import requests
from ..items import ImgtextItem
class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['desk.zol.com.cn','desk-fd.zol-img.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9684_117116_2.html']

    def parse(self, response):
        # 下一页需要点击按钮 按钮中有下一页的url 我们每次请求按钮中的下一页即可
        # 获取图片的地址
        # 使用图片管道 你提供url 他自动帮你下载
        url = response.xpath('//*[@id="bigImg"]/@src').get()
        next_url = 'https://desk.zol.com.cn/' + response.xpath('//*[@id="pageNext"]/@href').get()
        print(next_url)
        item = ImgtextItem()
        item['url'] = url
        print(1)
        yield item
        yield scrapy.Request(next_url,callback=self.parse)