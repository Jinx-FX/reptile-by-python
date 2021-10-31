# 目标
# 1.分析b站视频
# 2.下载b站视频
# 3.使用一个第三方的库 moviepy
#   作用： 提取视频  提取音频  合成视频

# 分析
# 1.播放电影的时候会请求电影所在的地址
# 2.在找视频地址的时候 我们通常直接在网页中打开来查看是不是视频地址，
# 这里有时候会访问不到 因为没有带上referer 就需要下载来查看
# 3.b站爬取的视频 没有声音 视频和音频是分开的
# 网络上的数据 是二进制数据 没有具体的格式
# 下载 查看到底是不是我们需要的数据
import requests
# url1 是视频的地址
url1 = 'https://xy182x103x238x111xy.mcdn.bilivideo.cn:4483/upgcxcode/31/53/222295331/222295331-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1621865192&gen=playurlv2&os=mcdn&oi=2936407749&trid=000168bb3d06b1ef4e39b7011974e00a4bfeu&platform=pc&upsig=4ca5079a1870803e37612bde6f3103ac&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=2000555&mid=0&bvc=vod&orderid=0,3&agrr=0&logo=A0000002'
url2 = 'https://xy111x72x11x83xy.mcdn.bilivideo.cn:4483/upgcxcode/31/53/222295331/222295331-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1621865192&gen=playurlv2&os=mcdn&oi=2936407749&trid=000168bb3d06b1ef4e39b7011974e00a4bfeu&platform=pc&upsig=98fa04de2c677c1f160a172e7e3ad72b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=8000025&mid=0&bvc=vod&orderid=0,3&agrr=0&logo=A0000080'
headers= {
    'referer': 'https://www.bilibili.com/video/BV1nE411f7NK?from=search&seid=1609354695342330255',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# 请求的是视频的地址
res = requests.get(url1,headers=headers)
# 保存视频地址
with open('a.mp4','wb') as f:
    f.write(res.content)

# 请求的是音频的地址
res2 = requests.get(url2,headers=headers)
# 保存音频地址
with open('a.mp3','wb') as f:
    f.write(res2.content)