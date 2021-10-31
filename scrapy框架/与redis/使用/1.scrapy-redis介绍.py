#  scrapy-redis 用来做分布式爬虫，可以实现高效率的爬虫

# 分布式：几台电脑同时干一件事情(类似于多任务)

#  scrapy-redis的实现 ： 把scrapy中的调度器和管道替换成了redis数据库
#   redis数据库需要实现的三点功能：
#      -  保存请求对象，分配任务
#      -  任务去重（断点续爬）
#      -  保存item对象
#

#  scrapy-redis只是替换了redis的几个组件，不是一个新的框架


#  redis服务器：master         SM
#              slaver
