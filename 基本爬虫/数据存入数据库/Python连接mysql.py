# -*- coding: utf-8 -*-
# pycharm 要使用专业版
# pip install pymysql
# 换源：pip install pymysql -i https://pipy.douban.com/simple
# ctrl + 鼠标左键 查看方法来源
# 1.导包
import pymysql
# 美化输出
from pprint import pprint

pymysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'mysql',
    'database': 'cq',
    'charset': 'utf8'
}

# 2.建立连接
conn = pymysql.connect(**pymysql_config)

# 3.创建游标对象 我们查询的数据 一些数据存在游标对象中
cur = conn.cursor()

# 4.使用execute对数据库进行操作
# cur.execute('select * from student')

# 5.拿去游标对象的结果
# res = cur.fetchone()
# print(res)
# res = cur.fetchmany(5)
# print(res)

# for i in cur.fetchall():
#     print(i)
# print('_'*100)
# print(cur.fetchall())
for i in range(14,100000):
    cur.execute('insert into student value(%s,"长清","一年级","六星教育",0,"男")'%i)

# cur.execute('delete from student where id = 13')
conn.commit()