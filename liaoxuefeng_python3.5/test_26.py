'''安装第三方模块'''

#通过包管理工具pip完成

#例：安装Pillow
#在命令行窗口输入pip install Pillow

#用pillow生成缩略图
from PIL import Image
im = Image.open('test.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')

#常用的第三方库还有MySQL的驱动：mysql-connector-python
#用于科学计算的NumPy库：numpy
#用于生成文本的模板工具：jinja2


'''模块搜索路径'''
#添加自己的搜索目录，有两种方法：
#1.直接修改sys.path，添加要搜索的目录，这种是在运行时修改，运行结束后失效
'''
import sys
sys.path.append('/Users/kurio/python_learning')
'''
#2.设置环境变量PYTHONPATH