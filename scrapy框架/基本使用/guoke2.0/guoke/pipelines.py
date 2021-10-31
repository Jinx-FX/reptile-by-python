# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class GuokePipeline:
    def __init__(self):
        self.file = open('wenda.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + ',\n')
        return item

    def __del__(self):
        self.file.close()
