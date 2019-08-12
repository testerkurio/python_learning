import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

# image = Image.open('/Users/gaojunjun/Downloads/code.png')
# text =pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4","99473","ad2488b5d8404dfd89c226cf35c1a52c" )
r.addFilePara("image", "D:/kurio/code.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text) # 返回信息
code_text = res.json()['showapi_res_body']['Result']
print(code_text)