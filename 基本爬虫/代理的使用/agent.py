# 代理：正向代理和反向代理

# 浏览器去访问服务器：一定是知道服务器的地址，所以使用代理去访问，代理也必须知道服务器的地址

#  正向代理：给客户端做代理，让服务器不知道客户端的真实身份
#  反向代理：给服务器做代理，让浏览器不知道服务器的真实地址
import requests

#  构造代理字典 #确定代理类型，用一个键值对就行 
proxies = {
    # "http": "http://123.55.101.65:9999",
    # "https": "https://119.179.160.153:8060",
    "http": "http://119.179.160.153:8060",
}

url = "https://www.baidu.com/"

# 请求的时候把proxies参数带进来
print(requests.get(url, proxies=proxies).content.decode())

# url = " "
#
# proxy = {
#     "http": "http://119.179.160.153:8060",
# }
#
# requests.get(url, proxies=proxy)
