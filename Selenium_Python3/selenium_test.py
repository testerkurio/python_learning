from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# import random
from PIL import Image
from ShowapiRequest import ShowapiRequest

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.5itest.cn/register")

# 获取验证码的图片
driver.save_screenshot("D:/kurio/register.png")
code_element = driver.find_element_by_id('getcode_num')
# print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
# print(code_element.size)
right = code_element.size['width'] + left
height = code_element.size['height'] + top
code_size = (left,top,right,height)
# print(code_size)
im = Image.open("D:/kurio/register.png")
# new_im = im.resize((1200,710),Image.ANTIALIAS)
code_img = im.crop(code_size)
code_img.save("D:/kurio/code.png")

# 识别验证码图片中的字符
r = ShowapiRequest("http://route.showapi.com/184-4","99473","ad2488b5d8404dfd89c226cf35c1a52c" )
r.addFilePara("image", "D:/kurio/code.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
# print(res.text) # 返回信息
code_text = res.json()['showapi_res_body']['Result']
print(code_text)

# 将用户信息填入到网页中的输入框中
driver.find_element_by_id('register_email').send_keys('kuriollr@163.com')
driver.find_element_by_id('register_nickname').send_keys('kurio')
driver.find_element_by_id('register_password').send_keys('kurio123')
driver.find_element_by_id('captcha_code').send_keys(code_text)

# driver.close()