# 点击应用可以查看有哪些数据
# fiddler每个响应点击一下看看在那里有我们的数据
# 如果是get请求 在浏览器中尝试打开
# 手机点击应用  应用去服务器获取数据  获取的过程中经过fiddler
# fiddler保存响应  爬虫去分析fiddler里面的响应

import requests
import jsonpath
import json
url = 'https://api-litchi.jstv.com/v6s/nav/10000858?OrderIndex=0&channel=0&pagesize=30&gid=60f1898ecaee&AppID=litchiV5&Sign=1c8b627864f044dc5c12e3226dbb30f7&TT=1961250705'
url = 'https://api-litchi.jstv.com/v6s/nav/14642?OrderIndex=0&channel=0&pagesize=30&gid=60f1898ecaee&AppID=litchiV5&Sign=63f1adde810d7467e3ce18b0dcab33ff&TT=-1209512047'
headers = {
'client': 'android',
'Host': 'api-litchi.jstv.com',
'User-Agent': 'okhttp/3.9.0'

}
res = requests.get(url,headers=headers)
print(res.content.decode())

titles = jsonpath.jsonpath(json.loads(res.content.decode()),'$..Title')
print(titles)
hrefs = jsonpath.jsonpath(json.loads(res.content.decode()),'$..Href')
print(hrefs)
