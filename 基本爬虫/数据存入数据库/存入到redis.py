import requests
import json
from jsonpath import jsonpath
import redis
import time
count = 1
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'referer': 'https://ke.qq.com/course/380991?taid=11424578648002623'
}
conn = redis.StrictRedis(db=8,decode_responses=True)


# for i in range(5):
#     url = f'https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page={i}&filter_rating=0&bkn=&r=0.012268771258203026'
#     res = requests.get(url,headers=headers)
#     datas = jsonpath(json.loads(res.content.decode()),'$..first_comment')
#     # 所有人的名字
#     nick_names = jsonpath(json.loads(res.content.decode()),'$..nick_name')
#     time.sleep(1)
#     for i in range(10):
#         print(nick_names[i])
#         print(datas[i])
#         conn.hset('hasha',nick_names[i],datas[i]) #存入数据

print(conn.hgetall('hasha')) #在redis里面是二进制形式，可以在py程序里面查看数据
# key:  key :vlaue

