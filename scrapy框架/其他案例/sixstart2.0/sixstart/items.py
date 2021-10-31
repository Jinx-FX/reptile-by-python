# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SixstartItem(scrapy.Item):
    # define the fields for your item here like:
    # 预处理 预先处理数据 这里面有的才能使用
    name = scrapy.Field()
    title = scrapy.Field()
    synopsis = scrapy.Field()

