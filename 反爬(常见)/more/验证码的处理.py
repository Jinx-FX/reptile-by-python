# 解决验证码
# requests 发送一次请求 页面中验证码会改变 很少用来解决验证码
# selenium 自动化  自动打开浏览器 截图
# 识别验证码图片 可以使用打码平台来解决验证码识别问题 需要钱
# 你把图片 读出交给超级鹰  超级后台代码 自动识别 识别完了后 把数据返回给你
# 接口就是方法 别人提供的方法
# 调用超级鹰把图片放进去 别人把验证码结果给我
# selenium 截图 是会根据电脑的分辨率 和 网页的大小来决定截图的位置
from PIL import Image
from selenium import webdriver
from chaojiying import Chaojiying_Client
import time
driver = webdriver.Chrome()
driver.get('http://www.chaojiying.com/user/login/')

# 截图 首先要网页全屏 防止没有截到指定的数据
# 浏览器的最大化
driver.maximize_window()

# 全屏后截图
driver.save_screenshot('chaojiying.png')

# 通过xpath定位到验证码的位置
imageElement = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img')
# imageElement.screenshot('chao.png')  直接定位到图片 截图 更加简单一点
# location 获取元素的xy轴
location = imageElement.location
print(location)  # {'x': 1110, 'y': 291}
# 获取长宽
size = imageElement.size
print(size)   # {'height': 50, 'width': 180}

# 截图 图片中的      坐标 和    长    宽
rangle = (location['x'],location['y'],location['x']+size['width'],location['y']+size['height'])

# 保存验证码
# 先读取一个文件
img = Image.open('chaojiying.png')
# 读取这个文件后 进行截图  需要把位置 和截图的大小放进去
img_data = img.crop(rangle)
# 截图后进行保存
img_data.save('yzm.png')

# 上面获取到了验证码后 使用打码平台进行识别
chaojiying = Chaojiying_Client('changqing', 'qwe123', '96001')  # 用户中心>>软件ID 生成一个替换 96001
im = open('yzm.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
yzm_data = chaojiying.PostPic(im, 1902)['pic_str']
print(yzm_data)
# 写入账号密码验证 点击登录
# 输入账号
driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('changqing')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('qwe123')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(yzm_data)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()