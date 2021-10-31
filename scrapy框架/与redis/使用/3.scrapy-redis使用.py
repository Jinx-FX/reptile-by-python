"""
在settings中修改五行：
#  把scrapy中默认的去重组件替换为scrapy-redis中的去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#  把scrapy中默认的调度器替换成scrapy-redis中的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#  任务持久化
SCHEDULER_PERSIST = True

#  添加scrapy-redis管道
ITEM_PIPELINES = {
    # 'guoke.pipelines.GuokePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,

}

# 添加redis数据库的连接URL
REDIS_URL = 'redis://user:pass@hostname:9001'



在spiders中要修改的部分：
    - 修改继承的类
    - 添加redis_key
    - 删除start_urls


在本地运行scrapy，直到redis服务器中 redis_key对应的value有值，整个scrapy-redis就会跑起来
"""
