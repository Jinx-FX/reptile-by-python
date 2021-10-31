# http://www.zanqianba.com/ #

# https://blog.csdn.net/qq_39881679/article/details/92828373?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522159343218919724839247822%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=159343218919724839247822&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-3-92828373.first_rank_ecpm_v3_pc_rank_v2&utm_term=%E8%80%83%E6%8B%89%E8%A7%A3%E6%9E%90

# https://v.douyin.com/J1Frqxw


import requests
import hashlib
import base64


# def parse_video(douyin_url):
#     pass
#     return 'xxx.com'

#转化为响应网站对应的base64加密，把base64翻转过来
def base64encode(text: str, reverse_map: bool = False) -> str:
    if reverse_map is False:
        return base64.b64encode(text.encode()).decode()

    base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="[::-1]

    r = ""  # the result
    c = 3 - len(text) % 3  # the length of padding
    p = base64chars[-1] * c  # the padding
    s = text + "\0" * c  # the text to encode

    i = 0
    while i < len(s):
        if i > 0 and ((i / 3 * 4) % 76) == 0:
            r = r + "\r\n"

        n = (ord(s[i]) << 16) + (ord(s[i + 1]) << 8) + ord(s[i + 2])

        n1 = (n >> 18) & 63
        n2 = (n >> 12) & 63
        n3 = (n >> 6) & 63
        n4 = n & 63

        r += base64chars[n1] + base64chars[n2] + base64chars[n3] + base64chars[n4]
        i += 3

    return (r[0: len(r) - len(p)] + p).lower()



# 点击解析视频，寻找响应里面的数据参数
#  确定url
url = 'http://www.zanqianba.com/parse/apply'

#  构造参数   # 多光标编辑：按住alt 点击鼠标左键
form_data = {
    "pageUrl": "https://v.douyin.com/J1Frqxw",
    "t": "1593435879991",
    "s": "097fon3by94h0t8hy9/aokwj09vezqvbz9kh064noa4a"
}

# 发送请求
# response = requests.post(url, data=form_data)

# vars/var *** 网页响应里面.js对应的变量

# ss = bb(cc.m(ss+tt))  # 调用bb函数，传入cc.m(ss+tt)的返回值
"""
tt = 1593435879991
ss = https://v.douyin.com/J1Frqxw

"""
md5_ret = hashlib.md5("https://v.douyin.com/J1Frqxw1593435879991".encode()).hexdigest()
print(md5_ret)  # 01ac2e82911980fcd704b5de4790b3bb
# s = base64(md5_ret)
# def bb(i) {
#     return cc.b.stringify(cc.u.parse(i), true).toLowerCase()
# }
print(base64encode("01ac2e82911980fcd704b5de4790b3bb", True).lower())

#  python实现base64


def get_s(douyin_url):
    s = ""
    return s
