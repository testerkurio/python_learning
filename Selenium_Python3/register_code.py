from selenium import webdriver
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time

driver = webdriver.Chrome()

def driver_init():
    driver.get('http://www.5itest.cn/register')
    # driver.maximize_window()

def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('123456789abcdefg',8))
    return user_info

# 获取验证码图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    code_img = im.crop((left,top,right,height))
    code_img.save(file_name)

# 解析验证码图片获取验证码
def analysis_code(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4","99473","ad2488b5d8404dfd89c226cf35c1a52c" )
    r.addFilePara("image", file_name)
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    code_text = res.json()['showapi_res_body']['Result']
    return code_text

# 运行主程序
def run_main():
    file_name = "D:/kurio/register.png"
    user_name_info = get_range_user()
    user_email = user_name_info + '@163.com'
    driver_init()
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_name_info)
    get_element('register_password').send_keys('kurio123')
    get_code_image(file_name)
    code_text = analysis_code(file_name)
    get_element('captcha_code').send_keys(code_text)
    time.sleep(10)
    driver.close()

run_main()