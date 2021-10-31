from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import cv2
import time
import requests
import numpy as np
# opencv 计算机视觉
# pytorch nlp(自然语言处理)

# 1.创建浏览器
driver = webdriver.Chrome()
# 2.打开网址
driver.get('https://dun.163.com/trial/sense')
# 3.使用xpath点击滑动拼图
driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()
# 4.点击完成验证
time.sleep(1)
driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/span[1]').click()
time.sleep(1)
i = 1
while True:
    # 获取两张图片的地址
    big_img_src = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/img[1]').get_attribute('src')
    small_img_src = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/img[2]').get_attribute('src')

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 请求图片地址进行下载
    big_res = requests.get(big_img_src,headers=headers)
    small_res = requests.get(small_img_src,headers=headers)

    # 保存两张图片
    with open('big.png','wb') as f:
        f.write(big_res.content)
    with open('small.png','wb') as f:
        f.write(small_res.content)

    # 读取两张图片
    big = cv2.imread('big.png')
    small = cv2.imread('small.png')

    # 进行灰度处理
    big = cv2.cvtColor(big,cv2.COLOR_BGR2GRAY)
    small = cv2.cvtColor(small,cv2.COLOR_BGR2GRAY)

    # 去掉滑块的黑色部分 保存必须的部分
    small = small[small.any(1)]
    # 使用opencv图像匹配算法
    result = cv2.matchTemplate(big,small,cv2.TM_CCOEFF_NORMED)
    index_max = np.argmax(result)  # 用来返回最大的索引值
    # 反推最大值的二维位置
    x,y = np.unravel_index(index_max,result.shape)
    # 得到坐标后 操作滑块移动到指定位置
    # 获取滑块
    drop = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]/span')
    # 实例化
    action = ActionChains(driver)
    # 移动滑块到指定为止1
    action.drag_and_drop_by_offset(drop,xoffset=y,yoffset=0).perform()
    time.sleep(2)
    # 成功了如何跳出
    # 获取xpath xpath如果是验证成功就跳出循环
    success = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]/span[2]').text
    if success == '验证成功':
        break
    else:
        print('现在是第%s次测试完成，但是没成功'%i)
        i += 1