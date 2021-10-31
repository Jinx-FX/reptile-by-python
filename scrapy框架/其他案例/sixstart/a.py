# 使用方式
# 1.创建项目 scrapy startproject 项目名称
# 2.创建爬虫 scrapy genspider sixstarText xxxx.com
# 3.修改爬虫 sixstarText
# 4.运行 scrapy crawl sixstarText

# 注意
# spider里面的文件 要给管道保存起来 就需要返回一个变量 item
# item 是一个字典
# 使用管道的时候 要在settings中开启管道
