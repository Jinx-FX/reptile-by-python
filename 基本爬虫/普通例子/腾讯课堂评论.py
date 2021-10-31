import requests
import json
from jsonpath import jsonpath
import time
for i in range(5):
    url = f'https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page={i}&filter_rating=0&bkn=&r=0.012268771258203026'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'referer': 'https://ke.qq.com/course/380991?taid=11424578648002623'
    }
    res = requests.get(url,headers=headers)
    # print(res.content.decode())
    # jsonpath第一个参数 是字典
    data = jsonpath(json.loads(res.content.decode()),'$..first_comment')
    print(f'----{i+1}------')
    print(data)
    print(f'----{i + 1}结束------')
    time.sleep(1)

'''
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page=0&filter_rating=0&bkn=&r=0.012268771258203026
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page=1&filter_rating=0&bkn=&r=0.45081504793410887

elements里面可以用xpath
response里面是json 那就不能用xpath
requests请求只能请求response里面的数据 

element里面可以用xpath
response里面可以用xpath 那就是用xpath 
'''

