"""
redis是key-value数据结构，每一条数据都是一个键值对
键的类型是字符串
值的类型分为五种：
  - 字符串 string
  -  哈希  hash
  -  列表  list
  -  集合  set
  -  有序集合 zset


键命令：
keys * : 查看所有的key
keys name: 查看某个键是否存在
exists key : 判断某个key是否存在，返回布尔
type key : 查看某个键对应的值的类型
del key : 删除一个键值对
expire key second : 给一个键值对设置有效期
ttl key : 查看某个key的有效期


string 字符串类型：redis的基本类型

set key value   : 设置键为key，值为value的数据
setex  key second value :  添加一个有效期为second秒的键值对
mset key1 value1 key2 value2 :一次性设置多个键值对
append key value :  在key对应的值后面追加value
get key: 获取某个key对应的value
mget key1 key2 key3 : 获取多个key对应的value


hash：哈希类型 用于存储对象，对象的结构为属性和值

hset key field value  :  设置一个键值对   {"bobo":{"age":"17","gender":"男"}}
hmset key field1 value1 field2 value2  ： 对于一个key，在他们的value中一次性设置多个属性
hget  key  field:  获取到 key的一个属性
hmget key field1 field2 : 获取key的多个属性
hkeys key :  获取某个key所有的属性名称
hvals  key :   获取某个key的所有value
hdel key field1 field2 : 删除某个key中指定的属性


list  : 列表类型  按照插入的顺序来排序

lpush key value1 value2  : 从左侧插入元素
rpush key value1 value2  : 从右侧插入元素
linsert key before/after  old new :   在旧的元素前面/后面添加新元素
lrange key start end : 查询两个下标之间的所有元素
lset key index value : 修改特定下标的元素值
lrem key count value : count=0时候，删除所有该元素，count为正数时，从前往后删除多少次， count为负数时，从后往前删除多少次，


set 无序集合 元素具有唯一性 不重复 对于集合没有修改操作

sadd key value1 value2 value3 : 向集合中添加元素
smembers key : 获取集合的所有元素
srem key member:  删除集合中的一个成员


zset 有序集合 元素具有唯一性 不重复 每个元素会关联一个score 代表权重

zadd key score1 member1 score2 member2 : 添加多个元素，分数在前
zrange key start stop : 返回指定下标内的元素
zrangebyscore key score1 score2 : 返回权重在两个分数范围内的元素
zscore key member : 获取某元素的分数
zrem key member1 member2  : 删除指定元素
zremrangebyscore key score1 score2 : 删除分数在范围内的所有元素


"""
