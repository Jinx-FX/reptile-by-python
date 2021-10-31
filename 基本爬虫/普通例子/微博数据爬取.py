# 开启fiddler 可能会让爬虫获取不到数据

import requests
import json
import jsonpath

# 确定微博热搜排行榜url
url = 'https://api.weibo.cn/2/page?networktype=wifi&extparam=seat%3D1%26dgr%3D0%26pos%3D0_0%26position%3D%257B%2522objectid%2522%253A%25228008643010000000000%2522%252C%2522name%2522%253A%2522%255Cu957f%255Cu6c99%2522%257D%26mi_cid%3D100103%26cate%3D10103%26filter_type%3Drealtimehot%26c_type%3D30%26display_time%3D1623071638&page_reform_enable=1&sensors_device_id=2af93bfe35607221&page_interrupt_enable=1&orifid=231619&uicode=10000011&moduleID=708&feed_mypage_card_remould_enable=true&just_followed=false&wb_version=4033&lcardid=hot_search&c=android&s=b7acab7f&ft=0&ua=Netease-MuMu__weibo__9.8.4__android__android6.0.1&wm=2468_1001&aid=01A1a9v_g6aWi6uf9TUzfNIwVT7OtuwMWVQLBIz0yGUuzzAB0.&ext=orifid%3A231619%7Coriuicode%3A10000010&fid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&v_f=2&v_p=76&from=1098495010&gsid=_2A25NuY0HDeRxGeBO6VsV8S3JzT6IHXVs7ofPrDV6PUJbkdB-LVClkWpNSja3RGFlPlubqxak0S0gLTZAdxIXoA4-&imsi=&lang=zh_CN&lfid=231619&page=1&skin=default&count=20&oldwm=2468_1001&sflag=1&oriuicode=10000010&containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&ignore_inturrpted_error=true&luicode=10000010&sensors_mark=1&android_id=2af93bfe35607221&header_skin_enable=0&sensors_is_first_day=true&cum=32FC78D5'

# 请求头
headers =  {
    'Host': 'api.weibo.cn',
    'Connection': 'keep-alive',
    'X-Sessionid': '1aea083e-f70e-43cf-b275-2d2e2da5737a',
    'User-Agent': 'MuMu_6.0.1_weibo_9.8.4_android',
    'X-Validator': 'IY78MwAkGWYZ1mjkVOhJ4pKQt0Dlkl3kCMnkGMZ05Tc=',
    'X-Log-Uid': '6029413562',
    'Accept-Encoding': 'gzip, deflate'
}

# 发起请求
res = requests.get(url,headers=headers)
print(res.content.decode())
titles = jsonpath.jsonpath(json.loads(res.content.decode()),'$..cards[0].card_group[*].desc')
desc_extrs = jsonpath.jsonpath(json.loads(res.content.decode()),'$..cards[0].card_group[*].desc_extr')
print(len(titles[1:]))
print(len(desc_extrs))
list_data = []
for desc_extr in desc_extrs:
    if desc_extr.isdigit():
        list_data.append(desc_extr)
    else:
        list_data.append(desc_extr.split('[')[0])
print(list_data)

dict_data = dict(zip(titles[1:],list_data))

print(dict_data)  # 有的值是空的

# 创建了新字典
new_dict = {}
for key in dict_data:  # 遍历字典 是key
    # 判断字典的值为True 如果是空的话 为False
    if dict_data[key]:  # 值不为空的时候执行
        # 新创建的字典   # zip压缩后的字典的值value
        # 给新字典创建key 设置value  i是新字典的key
        value = dict_data[key]
        new_dict[key] = value
print('-'*100)
print(new_dict)