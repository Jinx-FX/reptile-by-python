import redis

# db = database 使用5号数据库
conn = redis.StrictRedis(db = 5,decode_responses=True)
# conn.set('name','长清')
# res = conn.get('name')
# print(res)

# conn.rpush('list_1', 1, 2, 3, 4, 5, 6)
# res = conn.lrange('list_1', 0, 100)
# print(res)

# res = conn.keys()
# print(res)

conn.mset({'name':'cq','age':'19'})