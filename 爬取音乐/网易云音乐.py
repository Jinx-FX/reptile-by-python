# 爬取一个音乐
# vip  使用服务器中的数据库 设置字段为True 每次检测你就爬不了
# url用来定位网络资源
# 当我点击播放 就会去网络上请求音乐所在的地址 让数据返回给我前端

# 进入页面 按f12 清空所有响应 点击播放 此时就会加载音频地址
# 分析具体音频地址是什么

# 批量爬取 接口 地址 + 歌曲的id  直接定位到数据


import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
# 1.确定url   m4a或MP3后缀等
url = 'https://audio04.dmhmusic.com/71_53_T10050820325_128_4_4_0_sdk-cpm/cn/0103/M00/10/23/ChR45V8hZ6KACvl9AAdXWyWLTcg428.mp3?xcode=210fcd9f58d4d84f84346bb43667ca2cee64144'
# 2.发送请求 获取响应
res = requests.get(url,headers=headers)
print(res.content)

# 3.保存数据
with open('t.mp3','wb') as f:
    f.write(res.content)