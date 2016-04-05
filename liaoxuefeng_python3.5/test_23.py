'''装饰器'''

#函数对象由一个__name__属性，可以拿到函数的名字
def now():
	print('2016-4-5')
f = now
print(f())
print(now.__name__)
print(f.__name__)

'''
加入我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。
'''
#定义一个能打印日志的decorator
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

#接受一个函数作为参数，并返回一个函数。使用python的@语法，把decorator置于函数的定义处：
@log #把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
def now():
	print('2016-4-5')

#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
print(now())


'''如果decorator本身需要传入参数，则需要编写一个返回decorator的高阶函数，比如，要自定义log的文本：'''

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator #decorator再调用返回的函数，参数是now函数

@log('execute') #now = log('execute')(now)
def now():
	print('2016-4-5')

print(now())
print(now.__name__) 
'''
经过decorator装饰后的函数，__name__已经从'now'变为'wrapper'，
所以需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
可引用import functools模块，在def wrapper(*args,**kw)前加上@functools.wraps(func)
'''
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2016-4-5')

print(now())
print(now.__name__) 


'''习题1'''
#编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin call %s():' % func.__name__)
		func(*args,**kw)
		print('end call %s():' %func.__name__)
	return wrapper

@log
def now():
	print('2016-4-5')

print(now())


'''习题2'''
'''写一个@log的decorator，使它既支持：

@log
def f():
    pass

又支持：

@log('execute')
def f():
	pass
'''
import functools
def log(text = "call"): #设置默认text值为call
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print("%s:%s()" %(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator if not callable(text) else log()(text) #用callable()函数判断传入的是否为函数

@log
def now():
	print('1234')
print(now())

@log('hello')
def now():
	print('5678')
print(now())