# 什么是crawlspider：scrapy中的另外一种模板

#  crawlspider的作用：方便我们提取url，把yield Request对象的过程简单化

#  实现的原理：LinkExtractor能够帮助我们快速的提取url

#  如何创建一个crawlspider:
#  scrapy genspider -t crawl appname xxx.com

#  cralspider的特点：
#   1.继承的类不同
#   2.多了一个rule元组，元组中是Rules对象，包含三个参数 ：
#       - LinkExtractor对象：LinkExtractor(allow=r'Items/')
#       - callback
#       - follow=True
#   3.把默认的parse方法改成了parse_item方法

# LinkExtractor:
#  - allow: 允许的正则表达式，满足正则匹配的url都会被提取到
#  - restrict_xpaths：允许的xpath表达式,满足正则的url都会被提取到
