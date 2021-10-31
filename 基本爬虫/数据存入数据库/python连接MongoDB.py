import pymongo
# 1.建立连接
client = pymongo.MongoClient()
# 2.连接数据库
db = client['cq']
# 3.连接集合
my_col = db['stu']

# 插入一条文档
# my_col.insert_one({'name':'长清'})
# my_col.insert_many([{'name': '九歌', 'age': 18, 'ps': '是一个小仙女'},
#                     {'name':'金龙','age':18,'ps':'jinlingqishichongzhongwu'}])

# 修改一条
# my_col.update_one({'name':'长清'},{'$set':{'name':'九歌'}})
# 修改多条
# my_col.update_many({'name':'长清'},{'$set':{'name':'九歌'}})

# 删除一条
# my_col.delete_one({'name':'九歌'})
# 删除多条
# my_col.delete_many({'name':'九歌'})
# 查询一条文档
# res = my_col.find_one()
# print(res)
# 查询多条文档
res = my_col.find()
for i in res:
    print(i)