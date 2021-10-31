import requests
import json
import jsonpath


# 1.与移动端建立连接（可以用手机模拟器） 利用wife建立
#     主机ip地址 （cmd在ipconfig里面查看） + 8888（fiddler的接口api）
# 2.在fiddler里面查看移动端的响应
# 3.解析数据

url = "https://api.taptapdada.com/app-top/v1/hits?from=0&limit=10&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D624%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D97cad4e7-657e-4066-a83c-9e0465aa01ac&type_name=android_reserve_cn"

"https://api.taptapdada.com/app-top/v1/hits?from=20&limit=10&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D624%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Ddefault%26UID%3D97cad4e7-657e-4066-a83c-9e0465aa01ac&type_name=android_reserve_cn"
print(requests.get(url, verify=False).content.decode('unicode_escape'))
