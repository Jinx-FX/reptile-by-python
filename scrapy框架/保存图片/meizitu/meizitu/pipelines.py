# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.http import Request


# class MeizituPipeline:
#     def process_item(self, item, spider):
#         return item

class MeinvImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):  #自定义下载方式，同时需要配置管道需要
        name = request.meta.get('name')
        # print(name)
        # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return '%s.jpg' % (name)

    def get_media_requests(self, item, info):
        name = item['name']
        return [Request(x, meta={'name': name}) for x in item.get(self.images_urls_field, [])]
