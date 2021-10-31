# 通过视频首页下载你需要的视频
# 直接输入url就可以下载视频
# 搜索视频和音频的地址
# 有时候搜索不到你需要的数据
# 搜索一部分
# 数据存放的地址 很多
import requests
import re
url = 'https://www.bilibili.com/video/BV1Mv411h79F?from=search&seid=1609354695342330255'
headers= {
    'referer': 'https://www.bilibili.com/video/BV1nE411f7NK?from=search&seid=1609354695342330255',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get(url,headers=headers)
print(res.content.decode())
print('-'*100)

# 获取到视频的地址
vio_url = re.findall(r'"baseUrl":"(.*?)",',res.content.decode())[0]

# 获取到音频的地址
aio_url = re.findall(r'{"id":30280,"baseUrl":"(.*?)"',res.content.decode())[0]


# 获取数据之后 需要请求下载
# 请求视频地址 保存为mp4格式
res_vio = requests.get(vio_url,headers=headers)
with open('a.mp4','wb') as f:
    f.write(res_vio.content)
# 请求音频地址 保存为mp3格式
res_aio = requests.get(aio_url,headers=headers)
with open('a.mp3','wb') as f:
    f.write(res_aio.content)

# 数据都下载好了
# 下面进行合成 ：把音频放到视频中

# 导包
from moviepy.editor import *
# 获取音频文件
aio_data = AudioFileClip('a.mp3')
# 获取视频文件
vio_data = VideoFileClip('a.mp4')
# 把视频和音频合到一起 把音频放到视频上
vio_clip = vio_data.set_audio(aio_data)  # 给视频文件设置音频
# 输出为mp4文件
vio_clip.write_videofile('bilibil.mp4')

# ts 文件视频 有一个总的收录文件 index.m3u8
