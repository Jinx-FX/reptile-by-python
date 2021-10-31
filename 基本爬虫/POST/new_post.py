import requests

# post请求：比get请求更加安全，数据是放在请求体中，常用于用户提交数据，比如登录注册等

#  get请求：向服务器要数据，参数放在url中(url参数)
#  post请求：向服务器提交数据，数据放在formdata中(表单)，post请求也可以有url参数

word = input('请输入查询的关键字： ')

# 确定url Request UPL
url = "https://fanyi.baidu.com/langdetect"

#  构造表单 
# langdetect
# 在浏览器检查network中寻找  //照抄浏览器
# From data         
data = {
    "query": word
}

ret_data = {
    'zh': "中文",
    'en':"英文"
}

# 发送请求，获取响应，把表单带入到请求中
# 返回一个字典
# print(ret_data[eval(requests.post(url, data=data).text)['lan']])

response = requests.post(url, data=data)
dict_data = eval(response.text)
ret = dict_data['lan']#提取字典中的“键值对”
print(ret_data[ret])

#eval:
#检测字符串中的有效数据类型并提取转化

# str_data = '{"name": "bobo", "password": "qiaomu"}'

# print(type(str_data))
# print(eval(str_data))
# print(type(eval(str_data)))

# #  eval :自动调整格式
