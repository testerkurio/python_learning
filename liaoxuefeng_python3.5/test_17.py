'''高阶函数'''

'''变量可以指向函数'''

print(abs(-10))

x = abs
print(x(-30))

'''函数名也是变量'''

#函数名abs可以看作变量，可以将其指向其他对象，那么abs()则不起作用

'''传入函数'''

#一个最简单的高阶函数
def add(x,y,f):
	return f(x) + f(y)

print(add(-5,6,abs))

#编写高阶函数，就是让函数的参数能够接收别的函数