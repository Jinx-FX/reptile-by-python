import requests
from lxml import etree
from pprint import pprint
import pymysql
import time

# 建立连接
mysql_config = {
    'host':'127.0.0.1',
    'port':3306,
    'user': 'root',
    'password': 'jinx',
    'database': 'july',
    'charset': 'utf8'
}
conn = pymysql.connect(**mysql_config)
# 创建游标对象
cur = conn.cursor()

# 源url
# url = 'https://www.liepin.com/'
# 使用的url
url = 'https://www.liepin.com/zhaopin'

headers = {
    'Cookie': '__uuid=1633675714099.09; __s_bid=2abdee6baa222e48bf5c99b1d8c5db192794; __tlog=1633679205005.31%7C00000000%7C00000000%7C00000000%7C00000000; acw_tc=276082a316336792054364364eaf538e7a1d40d906934f9108973357cbd2ab; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1633675715,1633677360,1633679208; __session_seq=11; __uv_seq=29; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1633679325',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.liepin.com/job/1943556609.shtml?d_sfrom=search_prime&d_ckId=2a644a170d1c5b550a25321ef5ae1b64&d_curPage=0&d_pageSize=40&d_headId=2a644a170d1c5b550a25321ef5ae1b64&d_posi=0',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"'
}

name = input('请输入想要查询的关键字： ')

for i in range(1):
    params = {
        'key':name,
        'currentPage':i,
    }

    res = requests.get(url,headers=headers,params=params)
    html = etree.HTML(res.content.decode())
    
    # 读取搜索栏下显示条目url
    data_urls = html.xpath('//div/a[@data-nick="job-detail-job-info"]/@href')
    # pprint(data_urls)
    
    count = 1
    
    for data_url in data_urls:
        detail = requests.get(data_url,headers=headers)
        detail_html = etree.HTML(detail.content.decode())
        # 读取数据
        # 将列表转化为字符串，避免列表为空读取方框
        data_title = ''.join(detail_html.xpath('//div/span[@class="name ellipsis-1"]/text()'))
        data_salary = ''.join(detail_html.xpath('//div/span[@class="salary"]/text()'))
        data_location = ''.join(detail_html.xpath('//div[@class="job-properties"]/span[1]/text()'))
        data_experience = ''.join(detail_html.xpath('//div[@class="job-properties"]/span[3]/text()'))
        data_education = ''.join(detail_html.xpath('//div[@class="job-properties"]/span[5]/text()'))
        data_company = ''.join(detail_html.xpath('//div[@class="name ellipsis-1"]/text()'))
        # normalize-space()去除 \r\n
        data_demand = detail_html.xpath('normalize-space(//dd[@data-selector="job-intro-content"]/text())')

        # 插入数据到数据库中    
        # 在这里两个字符串加上引号 用来区分和前面的数字
        cur.execute('insert into info value(%s,"%s","%s","%s","%s","%s","%s","%s");'
        %(count,data_title,data_salary,data_location,data_company,data_education,data_experience,data_demand))
        count += 1
    
    time.sleep(0.99)

# 提交到数据库中
conn.commit()
# 关闭
cur.close()
conn.close()

print("over!")