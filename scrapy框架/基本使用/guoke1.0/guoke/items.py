# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
"""items文件使用来定位数据的模型类"""

class GuokeItem(scrapy.Item):
    # define the fields for your item here like:
    # 明确需要保存的字段名称
    question = scrapy.Field()
    answer = scrapy.Field()
    # author = scrapy.Field()
    # pass
