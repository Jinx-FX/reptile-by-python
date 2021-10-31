import scrapy
import re
import json
import jsonpath
from ..items import SixstartItem
class SixstartextSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'sixstarText'
    # 域(域名 范围) 爬取的链接 不能超出这个域的范围
    allowed_domains = ['sixstaredu.com']
    # 开始的url
    start_urls = ['https://www.sixstaredu.com/teacher?page=%s'%i for i in range(1,5)]

    def parse(self, response):
        '''用来提取数据'''
        names = response.xpath('//*[@id="content-container"]/div/div[*]/div/div[1]/h3/a/text()').getall()
        titles = response.xpath('//*[@id="content-container"]/div/div[*]/div/div[1]/div/text()').getall()
        # 获取详情页的地址 来请求详情页的数据
        # 1.获取xpath  //*[@id="content-container"]/div/div[2]/div/div[1]/a/@href
        hrefs = response.xpath('//*[@id="content-container"]/div/div[*]/div/div[1]/a/@href').getall()
        # print(names)
        # print(titles)
        print(hrefs)
        for i in range(20):
            # 第一种方式 自己手动创建一个字典
            # item = {}
            # 第二种方式 实例化items 里面的类
            item = SixstartItem()
            item['name'] = names[i]
            item['title'] =titles[i].strip()
            # item['href'] =hrefs[i]
            # 2.把url进行拼接 成一个完整的url路径
            href_url = 'https://www.sixstaredu.com'+hrefs[i]+'/about'
            print(href_url)
            # scrapy.Request scrapy里面发送请求
            # callback 回调函数 选择你要调用的函数 meta传递参数 要用字典的方式
            yield scrapy.Request(href_url,callback=self.parse_detail,meta={'item':item})
        # yield在循环外面 先执行上面的循环完 item结果就只有最后一个
        # yield item
        # 翻页操作 如果有个xpath 可以一直翻页 xpath结构不改变 可以用这种方法
        # next_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').get()
        # # 拼接
        # next_url = 'https://movie.douban.com/top250'+next_url
        # yield scrapy.Request(next_url,callback=self.parse)

    # 自己定义一个方法
    def parse_detail(self,response):
        '''提取详情页中的个人介绍'''
        synopsis = response.xpath('//*[@id="content-container"]/div/p/text()').get()
        if not synopsis:
            synopsis = response.xpath('//*[@id="content-container"]/div/p[*]//text()').get()
        # 通过response数据 获取前面传递过来的item
        item = response.meta.get('item')
        item['synopsis'] = synopsis
        yield item