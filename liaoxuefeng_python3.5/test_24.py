'''偏函数'''

#通过设定参数的默认值，可以降低函数调用的难度，而偏函数也可以做到这一点

int('12345') #默认按十进制转换
int('12345',base=8) #默认按八进制转换
int('12345',16) #默认按十六进制转换

#可以定义一个int2()的函数，默认把base=2传进去
def int2(x,base=2):
	return int(x,base)

'''functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()'''
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))

'''functools.partial的作用就是，把一个函数的某些参数给固定住（）也就是设置默认值，返回一个新的函数'''