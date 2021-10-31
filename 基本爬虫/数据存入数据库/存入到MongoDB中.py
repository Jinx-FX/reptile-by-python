import pymongo
import requests
import json
from jsonpath import jsonpath
import time
count = 1
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'referer': 'https://ke.qq.com/course/380991?taid=11424578648002623'
}
list_data = []
for i in range(5):
    url = f'https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page={i}&filter_rating=0&bkn=&r=0.012268771258203026'
    res = requests.get(url,headers=headers)
    datas = jsonpath(json.loads(res.content.decode()),'$..first_comment')
    # 所有人的名字
    nick_names = jsonpath(json.loads(res.content.decode()),'$..nick_name')
    time.sleep(1)
    for i in range(10):
        dict_data = {}
        dict_data['name'] = nick_names[i]
        dict_data['data'] = datas[i]
    # dict_data = dict(zip(nick_names,datas))
        list_data.append(dict_data)
# print(list_data)
# 建立连接
conn = pymongo.MongoClient()
# 获取数据库
db = conn['jinx']
# 获取集合 或自己创一个（写入便会创建）
col = db['save']
# 数据存入到数据库中
col.insert_many(list_data)


