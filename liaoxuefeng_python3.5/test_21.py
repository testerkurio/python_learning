'''返回函数'''

#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
#通常情况下的求和函数
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
#如果不需要立刻求和，而是在之后代码中根据需要再计算，可返回求和的函数
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1,3,5,7,9)
print(f())
#相关参数和变量都保存在返回的函数中，这种程序结构称为“闭包”
'''当调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数，两个函数都不相等，
两次调用函数的调用结果互不影响。'''


'''闭包'''

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3 = count() #f1，f2，f3分别对应fs这个list中的三个元素
print(f1(),f2(),f3())
#f1() == f2() == f3()的原因在于返回的函数引用了变量i，但它并非立刻执行
#等三个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

'''返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量'''

'''如果一定要引用循环变量怎么办？
方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变'''
def count():
	def f(j):
		def g():
			return j*j
		return g #返回值是个函数
	fs = []
	for i in range(1,4):
		fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
	return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())
'''缺点是代码较长，可利用lambda函数缩短代码'''