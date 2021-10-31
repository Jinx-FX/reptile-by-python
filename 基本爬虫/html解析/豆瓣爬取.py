# 1. 需要爬取豆瓣详情页的豆瓣评论
# 2. 怎么获取豆瓣详情页 //*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/a/@href
# 3. 获取页面中的评论 //*[@id="hot-comments"]/div[*]/div/p/span/text()

import requests
from lxml import etree
import time
url = 'https://movie.douban.com/top250'

headers = {
    'Cookie': 'bid=YLrkPuYddkk; dbcl2="193306366:LQoyh/2zrBY"; ck=D-xG; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1621254940%2C%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%5D; _pk_id.100001.4cf6=24e53461c325b146.1621254940.1.1621254940.1621254940.; _pk_ses.100001.4cf6=*; __utma=30149280.2104061185.1621254940.1621254940.1621254940.1; __utmb=30149280.0.10.1621254940; __utmc=30149280; __utmz=30149280.1621254940.1.1.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1606800148.1621254940.1621254940.1621254940.1; __utmc=223695111; __utmz=223695111.1621254940.1.1.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=223695111.1.10.1621254940; push_noty_num=0; push_doumail_num=0; __yadk_uid=5MHpXRFMHwBzKfSPF0Sn4jbJiuZjRY5X; __gads=ID=35405178d2b29d8a-22b193e6afc800fb:T=1621254940:RT=1621254940:S=ALNI_MaAR_jFLaSkVHsP8lvZdCa6nU9g_Q',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
list_data = []
b = 0
for i in range(3):  # 0 1 2  翻页
    params = {
        'start':i*25
    }
    # 发送第一次请求 请求top250
    res = requests.get(url,headers=headers,params=params)
    # 获取element数据
    html = etree.HTML(res.content.decode())
    # 通过xpath解析 解析多个url
    data_urls = html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[1]/a/@href')
    print(data_urls)
    # 通过xpath提取出标题  多个标题
    titles = html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a/span[1]/text()')
    print(titles)
    a = 0
    # 定义一个空列表来存放 后面添加的字典数据
    for data_url in data_urls:  # 第一次就是第一个链接 第二次就是第二个链接
        # 请求详情页的链接
        detail = requests.get(data_url,headers=headers)
        # 把详情页的数据转换为element数据方便我们使用xpath
        detail_html = etree.HTML(detail.content.decode())
        # 提取详情页中的评论
        data = detail_html.xpath('//*[@id="hot-comments"]/div[*]/div/p/span/text()')
        # 打印评论
        # print(data)
        # 定义一个字典
        dict_data = {}
        dict_data['title'] = titles[a]
        dict_data['commet'] = data
        print('这是第%s次数据：%s'%(b+1,dict_data))
        list_data.append(dict_data)
        time.sleep(0.99)
        a += 1
        b += 1
    print('最后')
    print(list_data)
# {'肖申克的救赎':['策划了19年的私奔……', '超级喜欢超级喜欢,不看的话人生不圆满.', '人的生命不过是从一个洞穴通往另一个世界..然后在那个世界的雨中继续颤抖.i hope', '没有人会不喜欢吧！书和电影都好。', '因为1994年台湾引进了一部比较卖座的老片The Sting，被错译成了《刺激》。到了1995年本片上映时，片商觉得其剧情与《刺激》有类似的地方（大概都属于高智商的复仇？），因此被译成了《刺激1995》，1998年又有一部片子Return To Paradise因为含有牢狱情节，被译成《刺激1998》！']}
# {title:'肖申克的救赎',comment:['策划了19年的私奔……', '超级喜欢超级喜欢,不看的话人生不圆满.', '人的生命不过是从一个洞穴通往另一个世界..然后在那个世界的雨中继续颤抖.i hope', '没有人会不喜欢吧！书和电影都好。', '因为1994年台湾引进了一部比较卖座的老片The Sting，被错译成了《刺激》。到了1995年本片上映时，片商觉得其剧情与《刺激》有类似的地方（大概都属于高智商的复仇？），因此被译成了《刺激1995》，1998年又有一部片子Return To Paradise因为含有牢狱情节，被译成《刺激1998》！']}


'''
第一页 https://movie.douban.com/top250?start=0    0*25  
第二页 https://movie.douban.com/top250?start=25   1*25
第三页 https://movie.douban.com/top250?start=50   2*25
r 读 w覆盖 a追加 
'''

a = [{'title':'a','b':'1'},{'title':'a','b':'1'}]