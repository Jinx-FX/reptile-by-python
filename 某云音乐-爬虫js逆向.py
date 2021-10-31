from Crypto.Cipher import AES  # 需要单独安装. pip install pycryptodome
import json
import base64  # a-zA-Z0-9+=
import requests


# 对数据进行加密
def enc(data):
    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = '0CoJUm6Qyw8W8jud'
    i = "f3j6zRVKAcXZqD4q"

    first = enc_one(data, g)

    encText = enc_one(first, i)
    encSecKey = '95147a1d5499edc3ae8f470d837a1681dcbc5ab6d7fdc84baaf91365fd7c8b18d766263a3bdbdd0a61a2a3db2bad7a672b20c040b2a455b5a9822e33407b567429db36d2d9bad79add7eb9f26e12ac6e37fdb7a5ffb2ce0b2cfb43a32be1b60b2dd3afd0a7163f394743ce720d295b04130aa756b50b7e6e9c548a6ad6497240'
    return encText, encSecKey


def to_16(bs):
    # 这里面选择使用PKCS7padding的填充逻辑(网易的逻辑)
    # 17 + ?15
    pad_len = 16 - (len(bs) % 16)
    # 填充的逻辑是: 需要补充的个数 * chr(需要补充的个数)
    bs += (pad_len * chr(pad_len)).encode()
    return bs


def enc_one(data, key):
    aes = AES.new(key=key.encode("utf-8"), IV=b"0102030405060708", mode=AES.MODE_CBC)
    bs = data.encode("utf-8")
    # 把字节填充成16的倍数
    bs = to_16(bs)
    enc_bs = aes.encrypt(bs)  # Data must be padded to 16 byte boundary in CBC mode

    # 把字节编码成base64的字符串
    b = base64.b64encode(enc_bs).decode()

    return b  # 暂时


# 发送请求
def main():
    url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
    data = {
        "csrf_token": "",
        "encodeType": "aac",
        "ids": "[1325905146]",
        "level": "standard",
    }
    data = json.dumps(data)
    encText, encSeckey = enc(data)

    resp = requests.post(url=url, data={"params":encText, "encSecKey": encSeckey})

    # 拿到歌曲下载的url
    download_url = resp.json()['data'][0]['url']
    print(download_url)

    with open("歌曲.m4a", mode="wb") as f:
        song_resp = requests.get(download_url)
        f.write(song_resp.content)


main()


""""
    
    function b(a, b) {  # a 是数据, b是秘钥
        var c = CryptoJS.enc.Utf8.parse(b)
        , d = CryptoJS.enc.Utf8.parse("0102030405060708")
        , e = CryptoJS.enc.Utf8.parse(a)  # e 也是数据
        , f = CryptoJS.AES.encrypt(e, c, {  # 对数据e进行加密. 用的是AES加密, c是秘钥
            iv: d,  # 偏移量 固定
            mode: CryptoJS.mode.CBC  # 模式是CBC
        });
        return f.toString()  # 注意, 这里返回的是字符串
    }
    
    function d(d, e, f, g) {  # 这里是加密的入口  d: 数据
        var h = {}
        , i = a(16);  # 固定16位的随机字符串
        h.encText = b(数据, g);
        h.encText = b(h.encText, i);
        h.encSecKey = c(i, e, f);
        return h
    }

"""
