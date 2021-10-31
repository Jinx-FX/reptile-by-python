# 分析 我们带的参数 有值是变动的
# 搜索这个值在那里 他是怎么产生的
# 先搜索elements有没有
# 搜索search 知道后 分析
# 分析sign才能解决js逆向问题 才能进行翻译
'''
salt: r.salt,   salt在r里面
 r = v.generateSaltSign(n)  鼠标引动过去可以看到一个方法 这里使用的就是这个方法

var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()   # 时间戳  13位
          , i = r + parseInt(10 * Math.random(), 10);   # 上面的时间戳 加上一个随机数
        return {
            ts: r,
            bv: t, 不要
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
                           # e 是我们输入的值   i 是上面的盐
        }
    };

'''
import time
import hashlib
import requests
import random
i = input('请输入你要查询的值：')
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
lts = str(int(time.time()*1000))
salt = lts + str(random.randint(0,9))

sign = hashlib.md5(("fanyideskweb" + i + salt + "Tbh5E8=q6U3EXe+&L[4c@").encode()).hexdigest()


data = {
    'i': i,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,                       # 这个值发生了变化
    'sign': sign,    # 这个值发生了变化
    'lts': lts,                         # 这个值发生了变化
    'bv': '24ecb70ba6203e4453baed50aa26b78e',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}

res = requests.post(url,headers=headers,data=data)

print(res.content.decode())
import re
re_data = re.findall(r'"tgt":"(.*?)",',res.content.decode())
print(re_data)