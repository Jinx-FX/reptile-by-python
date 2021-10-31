# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SixstartPipeline:

    def open_spider(self,spider):
        '''只会打开一次'''
        self.f = open('数据.txt','a',encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(str(item)+'\n')
        print(item)
        return item

    def close_spider(self,spider):
        '''只会关闭一次'''
        self.f.close()