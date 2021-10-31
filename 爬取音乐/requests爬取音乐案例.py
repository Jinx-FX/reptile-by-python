import requests
from lxml import etree
import jsonpath
import json


# 通过列表页获取到所有歌曲的id
# 根据歌曲id拼凑出包含歌曲下载地址的接口url
# 解析接口中歌曲的下载地址
# 下载歌曲

class BaiduMusic:
    def __init__(self):
        self.main_url = "http://music.taihe.com/top/dayhot"                  #https://music.taihe.com/songlist/281582

    def get_response(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        return requests.get(url, headers=headers).content

    def str_to_html(self, str_data):
        return etree.HTML(str_data)

    def parse_list(self, main_html):
        """解析列表页，返回所有歌曲的id信息"""
        ids = main_html.xpath("//span[@class='song-title ']/a[1]/@href")      # //div[@class='song-box']/a/@href
        names = main_html.xpath("//span[@class='song-title ']/a[1]/text()")   #//div[@class='song-box']/a/text()
        # print(len(res))
        # for num, i in enumerate(res):
        #     print(num, i)
        return [i.split('/')[-1] for i in ids], names

    def parse_detail(self, detail_text):
        """传入一个字符串类型，json格式的详情页响应，返回歌曲的下载链接"""
        dict_data = json.loads(detail_text)  # 字符串转字典
        download_url = ''.join(jsonpath.jsonpath(dict_data, '$..show_link'))
        return download_url

    def save(self, name, content, url):
        """传入名称和歌曲内容，保存歌曲"""
        with open(r"歌曲/" + name + '.mp3', 'wb')as f:
            f.write(content)
        print(f'歌曲{name} 保存完成', url)

    def main(self):
        main_html = self.str_to_html(self.get_response(self.main_url).decode())
        ids, names = self.parse_list(main_html)
        for id, name in zip(ids, names):
            detail_url = f"http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid={id}"
            detail_text = self.get_response(detail_url).decode()  # 字符串类型 json格式的响应
            download_url = self.parse_detail(detail_text)
            music_content = self.get_response(download_url)
            self.save(name.replace('/', '') if '/' in name else name, music_content, download_url)


if __name__ == '__main__':
    bdyy = BaiduMusic()
    bdyy.main()
# "http://audio04.dmhmusic.com/71_53_T10046233006_64_4_1_0_sdk-cpm/cn/0209/M00/66/6B/ChR47FsrtFyALYpSAA9L_U5ozXA.64.aac?xcode=8e36d4b006ed449a6976db141a6a8f1d2fb88c2"
# "http://audio04.dmhmusic.com71_53_T10046233006_64_4_1_0_sdk-cpmcn0209M00666BChR47FsrtFyALYpSAA9L_U5ozXA.64.aac?xcode=8e36d4b006ed449a6976db141a6a8f1d2fb88c2"
# "http://audio04.dmhmusic.com/71_53_T10046233006_64_4_1_0_sdk-cpm\/cn\/0209\/M00\/66\/6B\/ChR47FsrtFyALYpSAA9L_U5ozXA.64.aac?xcode=8e36d4b006ed449a6976db141a6a8f1d2fb88c2"