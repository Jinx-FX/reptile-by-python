# 对称加密 和非对称加密 单向加密（hashlib）
# 单向加密无法解密 大部分加密使用单向加密  登录的时候 用单向加密 ？？

import hashlib
# # md5 摘要算法  括号里面需要传入二进制数据
# a = '长清大帅哥132131412'
# res = hashlib.md5(a.encode())
# print(res)
# # hexdigest 转化为16进制（0-9 a-f） 32个字符串  常用
# # digest 转化为二进制字符串 不常用
# print(res.hexdigest())
# # print(res.digest())

# md5 加密图片
# with open('六星.png','rb') as f:
#     data = f.read()
#     print(data)
#
# res = hashlib.md5(data)
# print(res.hexdigest())

# 1.加密后的值是一样的 我这里123加密和你123加密一样
# 2.先把常用的值数字字母加密 保存到数据库中
# 3.下次有人来搜索我就能知道是什么
# 4.并不是解密 而是匹配
# 类似字典查询
# a = {'202cb962ac59075b964b07152d234b70':'123','7173c31f988286530001cb3231fc2838':'长清大帅哥'}
# data = input('请输入你要查询的值')
# # res = hashlib.md5(data.encode())
# print(a[data])

# md5加密 对二进制数据进行加密 变成字符串

# 加盐 在原来的基础上 加点东西
salt = '123hash'   # 123456长清大帅哥
res = hashlib.md5('579d9ec9d0c3d687aaa91289ac2854e4'.encode())
print(res.hexdigest())