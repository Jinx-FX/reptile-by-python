# md5：消息摘要算法

# MD5的特点： 1.不可逆：不能从密文推导出明文
#            2.不管明文长度为多少，密文的长度都固定
#            3.密文之间不会重复

# 使用场景： 密码加密    salt
#  username:bobo   password:xxxx.md5
#  123456qiaomu   "3b46f4e92cce717b885ae09f841eb838"

import hashlib

print(hashlib.md5('a'.encode()).hexdigest())
