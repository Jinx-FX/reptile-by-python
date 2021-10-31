from fontTools.ttLib import TTFont

# font = TTFont("fb471fefc3e6c5f635b6c765f116f1042280.woff")
# font = TTFont("b27abd92603f06fdf1cd46f2682a54912272.woff")
#  读取网站下载的字体文件

# font.saveXML('font2.xml')
#  把字体文件转成xml

#  下载font creator工具，把下载的字体放进去


"""
&#xf530; 1
&#xf530; 1
&#xf271; 2
&#xf30   7
"""

from lxml import etree

f = open('D:/python pro/requests_get_learning/反爬_常见/2.字体反爬/font2.xml', 'rb')

xml = etree.XML(f.read())
rets = xml.xpath("//psName/@name")[2:-2]
# print(rets)
# print(len(rets))

# for n in zip(rets,[i for i in range(11)]):
#     print(n)

f.close()
data = """('uniE65D', 9)
('uniEEF3', 8)
('uniE9E3', 3)
('uniF530', 1)
('uniF271', 2)
('uniF300', 7)
('uniE4C9', 5)
('uniEB4C', 0)
('uniF332', 4)
('uniE744', 6)
"""

font_map = {}

for i in data.splitlines():
    # print(i)
    font_map[eval(i)[0][3:]] = eval(i)[1]
print(font_map)

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Referer": "https://maoyan.com/",
    'Cookie': '__mta=143556490.1593608015536.1593608643220.1593610726080.6; uuid_n_v=v1; uuid=DF861C00BB9911EAA582DFDB8874C6699FF67E97834C4A779B2F6731292A431C; _csrf=258559d8b3a568a818de90c2f52f0a463da3bd289bb474b13add41c92712a0a1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593608015; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1730a708e0dc8-07ae78d7bef024-d373666-1fa400-1730a708e11c8; _lxsdk=DF861C00BB9911EAA582DFDB8874C6699FF67E97834C4A779B2F6731292A431C; __mta=143556490.1593608015536.1593608015536.1593608015536.1; mojo-uuid=02ae63af720280d194f3f37da2057ad7; mojo-session-id={"id":"055f55824d949341860a3ada01b2231f","time":1593610724951}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593610726; _lxsdk_s=1730a99e629-144-29-6c8%7C%7C3'

}

text = requests.get("https://maoyan.com/films/1298835", headers=headers).text

html = etree.HTML(text)
res = html.xpath("//span[@class='stonefont']/text()")
print(res)

#这是以前的代码，随着网站更新，对应情况可能不准





