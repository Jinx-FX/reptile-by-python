import requests
import json
from jsonpath import jsonpath
import pymysql
import time

class SaveMysql:

    def __init__(self,count,db,table):
        self.count = count
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'referer': 'https://ke.qq.com/course/380991?taid=11424578648002623'
        }
        mysql_config = {
            'host':'127.0.0.1',
            'port':3306,
            'user': 'root',
            'password': '13730612290JFX',
            'database': 'jinx',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**mysql_config)
        # 创建游标对象
        self.cur = self.conn.cursor()
        self.table = table
    def request(self):
        for i in range(7,9):
            url = f'https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page={i}&filter_rating=0&bkn=&r=0.012268771258203026'
            res = requests.get(url, headers=self.headers)
            self.datas = jsonpath(json.loads(res.content.decode()), '$..first_comment')
            # 所有人的名字
            self.nick_names = jsonpath(json.loads(res.content.decode()), '$..nick_name')
            time.sleep(1)
            self.save()

    def save(self):
        for i in range(10):  # 0~9  datas[0]  nick_names[0]
            # 插入数据到数据库中    # 在这里两个字符串加上引号 用来区分和前面的数字
            self.cur.execute('insert into %s value(%s,"%s","%s");' % (self.table,self.count, self.nick_names[i], self.datas[i]))
            self.count += 1

    def sucess(self):
        # 提交到数据库中
        self.conn.commit()
        # 关闭
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    my = SaveMysql(71,'jinx','comment')
    my.request()
    my.sucess()

#出错可能是原数据库 表中数据也需要设置为utf8
# 运行命令   mysql> alter table 表名 convert to character set utf8mb4;