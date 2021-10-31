# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

"""管道：用来保存数据"""

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class GuokePipeline:
    # def open_spider(self, spider):
    def __init__(self):
        """spider组件开启的时候，只执行一次"""
        print('---1---')
        self.file = open('wenda.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        """处理item，也就是保存数据的逻辑"""
        #  loads是把字符串转字典
        #  dumps是字典转字符串
        print('---2---')
        dict_item = dict(item)  # 把item转成字典格式
        self.file.write(json.dumps(dict_item, ensure_ascii=False) + ',\n')
        #  把字典转成字符串然后写入
        return item  # 把item输出到调试信息上

    # def close_spider(self, spider):
    def __del__(self):
        """spider组件关闭的时候执行，只执行一次"""
        print('---3---')
        self.file.close()
