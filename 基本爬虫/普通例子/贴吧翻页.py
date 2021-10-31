import requests
import time
# 确定url
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
for i in range(5):  # 0 1 2
    params = {
        'kw': '李毅',
        'pn': i*50
    }
    url = 'https://tieba.baidu.com/f?'
    # 发起请求 获取响应
    res = requests.get(url,headers=headers,params=params)
    # 写入到数据中
    with open('李毅_%s.html'%(i+1),'w',encoding='utf-8') as f:
        f.write(res.content.decode())
    time.sleep(1)
    print('成功爬取%s页'%(i+1))
'''
翻页：第一页网址 到第三页网址 分别的url是什么 然后再找规律 
第一页 https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&pn=0    0*50 
第二页 https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&pn=50   1*50
第三页 https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&pn=100  2*50
第四页 https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&pn=150  3*50 
'''

