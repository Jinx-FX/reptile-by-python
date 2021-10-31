import requests
import time
import hashlib
import base64

#获取时间戳
tt = str(int(time.time() * 1000)) 


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


def get_s(douyin_url):
    md5_ret = hashlib.md5((douyin_url + tt).encode()).hexdigest()
    s = base64encode(md5_ret, True)
    return s


douyin_url = input('请输入想要解析的抖音视频链接: ')

#  构造参数   # 多光标编辑：按住alt 点击鼠标左键
form_data = {
    "pageUrl": douyin_url,
    "t": tt,
    "s": get_s(douyin_url)
}

post_url = 'http://www.zanqianba.com/parse/apply'

headers = {
    "Cookie": "Hm_lvt_1ffb2a21976950f720cc69e0db4a1dfc=1621773094; tokens=7c6a6ea3a5e0aae72b3877dc97e4e242; Hm_lpvt_1ffb2a21976950f720cc69e0db4a1dfc=1621775804"
}

print(requests.post(post_url, data=form_data, headers=headers).text)
