# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['renren.com']

    # start_urls = ['http://xxx.com/']

    # def start_requests(self):
    #     """实现post请求的登录，把响应交给self.parse去处理"""
    #     login_url = 'http://www.renren.com/PLogin.do'
    #     data = {
    #         'email': '13142068390',
    #         'password': 'sixstar123'
    #     }
    #     #  构造一个POST请求对象，传入url，formdata和回调函数
    #     yield scrapy.FormRequest(login_url, formdata=data, callback=self.parse)  #方法一
    #     # yield scrapy.FormRequest.from_response(login_url, formdata=data, callback=self.parse) #方法二，较麻烦

    def start_requests(self):
        url = 'http://www.renren.com/972035912/newsfeed/photo'
        cookies = "anonymid=k9wp3w93-x9edch; _r01_=1; taihe_bi_sdk_uid=7ae8fff48a449d38ea5cb4dcf23526d9; jebe_key=551b7017-186c-4fa7-a0e7-062dad08b2c7%7C8da1fa8db318da7873743d11a45be0f9%7C1588851428340%7C1%7C1591103354085; jebe_key=551b7017-186c-4fa7-a0e7-062dad08b2c7%7C8da1fa8db318da7873743d11a45be0f9%7C1591797804818%7C1%7C1591797804871; __utma=151146938.1982388100.1591878891.1591878891.1591878891.1; __utmz=151146938.1591878891.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; depovince=GW; JSESSIONID=abcgmMCo1Frfl9mZKpinx; ick_login=48000c31-dba2-4c34-b4d3-c46014bd4dff; taihe_bi_sdk_session=c9f55f33d46dd3b3c1be0f26328e1902; first_login_flag=1; ln_uact=13142068390; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20200509/1835/main_NlVA_0abe0000454c195a.jpg; jebecookies=dcc75e3c-2de0-4ef6-ba78-6a9b6a74a1c6|||||; _de=2CF44FD0A730566B666DB61B73BDA9A9; p=909b5c29c9af41b791f313b90754f58f2; t=45bae8e11ff9f10d2be5d2339656a9882; societyguester=45bae8e11ff9f10d2be5d2339656a9882; id=972035912; xnsid=b7aad95e; loginfrom=syshome"
        cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in cookies.split("; ")}
        # yield scrapy.Request(url, callback=self.parse, cookies=cookie_dict, dont_filter=True) #dont_filter=True 不过滤相同请求的相应????

    def parse(self, response):
        # print(response.request.cookies)
        # print(response.body.decode())
        yield scrapy.Request('http://www.renren.com/972035912/newsfeed/photo', callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        print(response.body.decode())
        # pass
