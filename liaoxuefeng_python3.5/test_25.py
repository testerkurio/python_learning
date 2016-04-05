'''使用模块'''
#以内建的sys模块为例，编写一个hello的模块

#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a test module' #模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Kurio Liu'

import sys

def test():
	args = sys.argv 
	#argv变量用list存储了命令行的所有参数，运行python test_25.py kurio获得的sys.argv就是['test_25.py','kurio']
	if len(args) == 1:
		print('Hello,world!')
	elif len(args) == 2:
		print('Hello,%s!' %args[1])
	else:
		print('Too many arguments!')

#在命令行运行test_25模块时，python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该模块，if判断将失败
#因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
if __name__ == '__main__':
	test()


'''作用域'''

#在python中，通过_前缀来实现函数及变量的模块内部化
#正常的函数和变量名是公开的(public)，可以被直接引用，如abc，x123，PI等
#类似__xxx__是特殊变量，可以被直接引用，但是有特殊用途，自己的变量一般不要用这种变量名
#类似_xxx和__xxx这样的函数或变量就是非公开的(private)，不应该被直接引用，但不是不能被直接引用

def _private_1(name):
	return 'Hello,%s' %name
def _private_2(name):
	return 'Hi,%s' %name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
		
'''外部不需要引用的函数全部定义为private，只有外部需要引用的函数才定义为public'''