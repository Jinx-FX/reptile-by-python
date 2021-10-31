# get 一般用于请求服务器 获取数据 渲染页面 让页面展示出来
# post 用于携带一些参数 给后端（服务器） 一般拿到数据 可以存入数据库中 拿到数据可以进行验证
# 有些请求 你带参数 给他 他返回你要的数据 翻译 你给他中文 他给你英文 有些数据需要登陆后才能看到
# 翻译网站 https://www.iciba.com/fy

import requests
import re
# # 1.确定url
# url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=dbe03275e7157f02'
# # 2.发送请求 获取响应
# # 构建参数 使用页面上的参数
#
# data = {
#     'from': 'zh',
#     'to': 'en',
#     'q': '跳舞'
# }
# # data=data 这个是post请求所需要的参数
# res = requests.post(url)
# print(res.content.decode())
# response = re.findall(r'"out":"(.*?)",',res.content.decode())
# print(response)
url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=f89fdd5c67d695cb'
data = {
    'from': 'zh',
    'to': 'en',
    'q': '中文' 
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
res =requests.post(url,data=data,headers=headers)
print(res.content.decode())