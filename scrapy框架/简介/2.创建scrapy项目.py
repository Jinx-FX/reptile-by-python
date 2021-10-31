#   安装scrapy,一定要加镜像:  pip install scrapy -i https://pypi.douban.com/simple
#   必须加镜像，因为scrapy有一些依赖库需要手动安装，安装完以后才能安装scrapy
#   加镜像可以一步到位
#   
    # 终端对应文件目录
    # 以下命令都要加上“ python -m ” 表示python运行scrapy模块 

#  1.使用scrapy创建项目：
#       scrapy startproject pro_name
#  2.创建spider
#       cd proname, scrapy genspider spidername xxx.com
#  3.在spider中修改信息（allow_domains和start_urls）
#       allow_domains：允许的域，不在域的范围之内的url讲不会发送请求
#       start_urls：起始的url，第一个请求的url
#  4.编写items:
#        需要爬取哪些字段，在这里定义好
#  5.编写spider代码
#     - 默认的parse方法是对于start_urls请求的响应
#     - 构造item，然后yield item，会把item传递给管道
#  6.启动scrapy
#      scrapy crawl spidername --nolog (保证在根目录)(--nolog可以不显示调试信息，只显示我们自己定义的print)
#
#  7. 保存数据
#      在spider里面yield的item会传递到pipeline中来
#      需要在pipeline管道中定义数据的保存逻辑
#      def open_spider(self, spider): # 爬虫开启的时候执行一次，可以用来打开文件
#      def close_spider(self, spider):#  爬虫关闭的时候执行一次，用来关闭文件
#      process_item : 用来处理数据的保存
#      注意：一定要在settings中开启item_pipeline管道，这样管道才能生效

