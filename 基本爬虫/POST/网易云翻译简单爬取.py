import requests

# 确定url
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

# 使用headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Referer': 'https://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=559290507@10.169.0.84; JSESSIONID=aaa8FwFrlpT3NfzzFxcNx; OUTFOX_SEARCH_USER_ID_NCOO=2145560273.8152783; ___rl__test__cookies=1622463629112'

}
# 'i: 中文' === > 'i': '中文',
# 这是一个post请求  带上data参数
data = {
    'i': '中文',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16224628047061',                       # 这个值发生了变化
    'sign': 'f7166566b946a70b2f0a77c5fc8ae6ca',    # 这个值发生了变化
    'lts': '1622462804706',                         # 这个值发生了变化
    'bv': '24ecb70ba6203e4453baed50aa26b78e',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}

res = requests.post(url,headers=headers,data=data)
# 获取不到
print(res.content.decode())

# 我们在访问数据的时候 验证 有写值是变动的
# 登录 记录你的登录时间 2天后过期 或者使用时间戳