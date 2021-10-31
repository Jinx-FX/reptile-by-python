# 1.确定url，评论所在的url是那个
# 2.requests请求数据 下载
import requests
import re
url = 'https://api.bilibili.com/x/v2/reply/main?callback=jQuery17209117503056281779_1621428421907&jsonp=jsonp&next=0&type=1&oid=930552096&mode=3&plat=1&_=1621428423096'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'referer': 'https://www.bilibili.com/video/BV1XK4y1d7Tu?spm_id_from=333.851.b_62696c695f7265706f72745f6469676974616c.41'
}

res = requests.get(url,headers=headers)
print(res.content.decode())
data = re.findall(r'"content":{"message":"(.*?)",',res.content.decode())
print(data)