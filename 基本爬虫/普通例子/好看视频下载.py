import requests
from lxml import etree
url = 'https://haokan.baidu.com/v?vid=15209329785548664752&tab='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
# 请求首页
res1 = requests.get(url,headers=headers)
# 把首页数据转换为element数据
html = etree.HTML(res1.content.decode())
# 使用xpath提取element里面的视频地址
url2 = html.xpath('//*[@id="mse"]/video/@src')
print(url2)
# url = 'https://vd4.bdstatic.com/mda-mc4jh63h0a9bewtj/sc/cae_h264_clips/1614924223/mda-mc4jh63h0a9bewtj.mp4?auth_key=1621433391-0-0-2412964d71206d249fde5812f0b561f7&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest='
# 请求上面获取到的视频地址
res2 = requests.get(url2,headers=headers)
# 把视频数据保存起来 要注意视频是二进制的数据
with open('好看视频.mp4','wb') as f:
    f.write(res2.content)
'''
elements里面有我们要的值 
但是response里面没有 那么我们就获取不到自己要的值 
selenium 这个可以获取elements里面的值 

xpath和jsonpath都是工具不是类型 

html 一般可以用xpath
字典一般算是json 可以用jsonpath 

requests库的问题 他只能获取response响应 

使用requests获取好看视频首页的方式就不能获取视频 
elements和response里面的数据不一样 
'''