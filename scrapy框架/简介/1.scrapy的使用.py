#  scrapy框架：爬的快
#  为什么爬的快：因为底层使用了异步网络框架twisted

#  requests库已经能够完成绝大部分爬虫任务

#  框架：把很多功能和模块封装起来，留下一下可供我们调用的接口，我们就能够通过框架，快速的实现强大的功能

#  scrapy的组成部件：
#  1.引擎（engine）: 负责总体调度，scrapy的大脑
#  2.调度器（scheduler）： 1. 接收引擎(爬虫组件)发送过来的Requests对象，并且保存  
#                         2. 弹出Requests对象，交给引擎(下载器)
#  3.下载器（downloader）： 接收引擎（调度器）发过来的Requests对象，发送网络请求，
#                          并且获取响应，把响应交给引擎（爬虫组件）， response= requests.get(url)
#  4.爬虫组件（spiders）：接收引擎（下载器）传递过来的Response，同时解析response，
#                       1，把提取出的数据交给引擎（管道）
#                        提取出url，构造Requests请求，交给引擎（调度器）  xpath  json
#  5.管道（pipeline）： 保存数据

