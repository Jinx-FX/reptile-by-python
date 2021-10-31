# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# 导入图片管道类 方便我创建类的时候继承
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import requests
class ImgtextPipeline:
    def process_item(self, item, spider):
        # print(item['url'])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
        }
        res = requests.get(item['url'],headers=headers)

        imagename = item['url'].split('/')[-1]
        with open(imagename,'wb') as f:
            f.write(res.content)
        return item

# 创建图片管道
class ImgtextPipeline2(ImagesPipeline):

    def get_media_requests(self, item, info):
        '''用来请求数据'''
        # item['url'] 图片的url
        print(2)
        yield scrapy.Request(item['url'],meta={'item':item})

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta['item']
        imagename = item['url'].split('/')[-1]
        print(imagename)
        # print(num)
        # print(item)
        # print('---------------')
        # print(item2)
        # imgname = '美女图片.jpg'
        return imagename

    def item_completed(self, results, item, info):
        return item
