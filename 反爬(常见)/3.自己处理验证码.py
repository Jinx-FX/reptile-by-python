# 如果我们自己动手看验证码
import requests

url = "gushiwen.org"

session = requests.Session()

text = session.get(url).text 
#  解析响应，找到验证码的图片地址， src=

#  下载验证码图片，保存
with open('code.jpg', 'wb')as f:
    f.write('验证码的url地址'.encode())

code = input('验证码是: ')

login_url = "login.com"

data = {
    "username": 'xx',
    "password": 'xx',
    "code": code
}
requests.post(url, data=data)
