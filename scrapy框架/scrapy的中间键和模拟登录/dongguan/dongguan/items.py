# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 问题的标题
    ques_content = scrapy.Field()  # 问题的内容
    status = scrapy.Field()  # 问题的状态
    publish_time = scrapy.Field()  # 发布日期
    answer = scrapy.Field()  # 官方回复

