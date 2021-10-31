import requests
import json
from jsonpath import jsonpath
import pymysql
import time

count = 1
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'referer': 'https://ke.qq.com/course/380991?taid=11424578648002623'
}
# 建立连接
mysql_config = {
    'host':'127.0.0.1',
    'port':3306,
    'user': 'root',
    'password': '13730612290JFX',
    'database': 'jinx',
    'charset': 'utf8'
}
conn = pymysql.connect(**mysql_config)
# 创建游标对象
cur = conn.cursor()
for i in range(5):
    url = f'https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page={i}&filter_rating=0&bkn=&r=0.012268771258203026'
    res = requests.get(url,headers=headers)
    datas = jsonpath(json.loads(res.content.decode()),'$..first_comment')
    # 所有人的名字
    nick_names = jsonpath(json.loads(res.content.decode()),'$..nick_name')
    time.sleep(1)

    for i in range(10):  # 0~9  datas[0]  nick_names[0]
        # 插入数据到数据库中    
        # 在这里两个字符串加上引号 用来区分和前面的数字
        cur.execute('insert into comment value(%s,"%s","%s");'%(count,nick_names[i],datas[i]))
        count += 1                         #   1  '长清''评论'

# 提交到数据库中
conn.commit()
# 关闭
cur.close()
conn.close()
'''
数据存入到数据库中 
提前准备好数据 
0.id 序号 当做主键 
1.名字 
2.评论 
入库 

'''

#出错可能是原数据库 表中数据也需要设置为utf8
# 运行命令   mysql> alter table 表名 convert to character set utf8mb4;
