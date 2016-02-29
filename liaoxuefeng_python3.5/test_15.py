'''生成器'''

#一边循环一边计算的机制，称为生成器：generator

'''方法1'''
#把列表生成式的[]改成()，就创建了一个generator
L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
print(g)

#通过next()函数获得generator的下一个返回值
#print(next(g))

'''正确的方法应该是使用for循环来打印generator'''
for n in g:
	print(n)

#如果推算的算法较复杂，用类似列表生成式的for循环无法实现时，可用函数实现

'''菲波拉契数列'''
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b #即给a赋予b的值，给b赋予a+b的值
		n = n + 1
	return 'done'

print(fib(6))

'''方法2'''
#如果一个函数定义中包含yield关键字，那么这个函数就是一个generator
def fib2(max):
	n, a, b = 0, 0 ,1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

'''函数是顺序执行，遇到return语句或最后一行函数语句就返回；
但generator函数在每次调用next()的时候执行，遇到yield语句返回，再次执行时从
上次返回的yield语句处继续执行'''

for n in fib2(7):
	print(n)
#用for循环调用generator时，拿不到generator的return语句的返回值
#想要拿到返回值就必须捕捉StopIteration错误，返回值包含在StopIteration的value中
f = fib2(6)
while True:
	try:
		x = next(f)
		print('f:',x)
	except StopIteration as e:
		print("Generator return value:",e.value)
		break


'''习题'''

'''杨辉三角'''
def triangles():
	a = [1]
	while True:
		yield a
		a = [sum(i) for i in zip([0] + a, a + [0])]
		#[0]+a为[0,1]，a+[0]为[1,0]
		#zip([0,1],[1,0])=[(0,1),(1,0)]
		#i为[(0,1)]或[(1,0)]
		#[sum(i)]=[1,1]
		#a=[1,1]
'''
n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
'''
h = triangles()
for n in range(10):
	print(next(h))