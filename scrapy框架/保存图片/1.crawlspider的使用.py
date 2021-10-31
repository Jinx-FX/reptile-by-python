#  1.创建一个crawlspider  ： scrapy genspider -t crawl appname xxx.com

#  2.  rules() : 定义提取到的url构造成Request对象以后，请求发送和响应解析的规则

#  3. LinkExtractor()  什么样的url会被提取到
#       - allow:满足正则条件的url，会被提取出来
#       - restrict_xpaths: 满足xpath条件的url，会被提取出来
