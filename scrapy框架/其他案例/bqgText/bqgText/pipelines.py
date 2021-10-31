# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo
class Bqgtext2Pipeline:
    def open_spider(self,spider):
        # 建立连接
        self.conn = pymysql.connect(user='root',password="mysql",database='cq',charset="utf8")
        # 创建游标对象
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):

        # 使用游标对象的方法插入数据
        self.cur.execute('insert into bqg value("%s","%s")'%(item['title'],''.join(item['data'])))
        # 保存 提交
        self.conn.commit()
        return item
    def close_spider(self):

        # 关闭
        self.cur.close()
        self.conn.close()

class BqgtextPipeline:
    def process_item(self, item, spider):
        print(item)
        with open('%s.txt'%item['title'],'w',encoding='utf-8') as f:
            f.write(''.join(item['data']))
        yield item
