import time

import requests
import re
for i in range(1,10):
    # 确定url
    url = 'https://www.guokr.com/beta/proxy/science_api/articles?page=%s'%i
    headers ={
        'Referer': 'https://www.guokr.com/science/category/all',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    # 请求响应
    res = requests.get(url,headers=headers)
    # print(res.text)
    # 进行Unicode 解码  decode('unicode-escape') 以后遇到\u6b96 \u  decode默认是utf-8   unicode万国码
    if i == 1:      
        print(res.content.decode('unicode-escape'))
    else:
        print(res.content.decode())
    time.sleep(0.2)
    print('-'*10+'这是第%s页'%i+'-'*10)


'''
分析：
第一页：https://www.guokr.com/beta/proxy/science_api/articles?page=1
第二页：https://www.guokr.com/beta/proxy/science_api/articles?page=2
第三页：https://www.guokr.com/beta/proxy/science_api/articles?page=3
'''