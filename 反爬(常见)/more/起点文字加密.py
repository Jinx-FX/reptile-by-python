# 字体加密
# 在响应当中就会有一个字体文件 会形成映射表
# 网页中数据加密 加密前的字体数据 都会存在字体文件中  woff
# FontCreator软件用来查看字体文件
# 字体文件打开后 有名字对应值
# fontTools 需要通过pip
from fontTools.ttLib import TTFont
import requests
import re
# 确定你要的数据在那个网页汇总
url = 'https://book.qidian.com/info/1021617576'
# 获取名字对应的数据是什么
data  = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'period':'.'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

res = requests.get(url,headers=headers)
# print(res.content.decode())

# 获取到加密后的数据
font_data = re.findall(r'<span class=".*?">(.*?);</span></em><cite>万字',res.content.decode())[0]
woff_list = font_data.replace('&#','').split(';')
print(woff_list)

# 获取woff文件的url
woff_url = re.findall(r"format\('eot'\); src: url\('(.*?)'\) format\('woff'\),",res.content.decode())[0]
# print(woff_url)

# 获取连接后 请求连接 下载保存为woff
woff_data = requests.get(woff_url,headers=headers)

with open('字体文件存放.woff','wb') as f:
    f.write(woff_data.content)

# 读取字体文件
font = TTFont('字体文件存放.woff')
# 另存为xml数据
# font.saveXML('1.xml')
# getBestCmap 获取字体文件中的映射关系
cmap = font.getBestCmap()
print(cmap)

sum = ''
for i in woff_list:
    # 循环每一个加密后的数据 放到映射表中 获取到 数字对应的名字
     data_i = cmap[int(i)]
                # 通过名字获取你要的数字
     sum = sum + data[data_i]

print(sum)