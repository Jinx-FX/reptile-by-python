# 1.创建项目和appscrapy startproject,cd project, scrapy genspider appname xxx.com

#  2.修改allow_domains和start_urls

#  3.编辑items

#  4.编辑parse方法，解析起始url的响应，构造item，yield item

#  5.在管道中接收item 进行保存

#  6.爬取详情页：

#  用右键的方式启动scrapy  见start.py
#  from scrapy.cmdline import execute
# execute(("scrapy crawl wenda").split())      # 列表中 元素分割 输出命令

# scrapy feed export :  scrapy crawl appname -o file.json(csv)
#  settings中使用 FEED_EXPORT_ENCODING 设置保存文件的编码

#  scrapy调试工具：scrapy shell
# python -m scrapy shell 网站url   进入，直接使用代码语句检测
