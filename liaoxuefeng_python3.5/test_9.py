'''定义函数'''

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x


'''空函数'''

def nop():
	pass #可以用来作为占位符

#pass还可用在其他语句里
age = 20
if age >= 18:
	pass


'''参数检查'''

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>= 0:
		return x
	else:
		return -x


'''返回多个值'''

import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y) 
#返回多值其实就是返回一个tuple
#返回一个tuple可以省略括号
print(math.pi/6)
print(math.cos(math.pi/6))


'''习题'''

#ax² + bx + c = 0
import math

def quadratic(a,b,c=0):
	if a == 0:
		if b == 0:
			return TypeError('当a=0时,b不能为0')
		else:
			x = -c/b
			return x
	elif b*b < 4*a*c:
		return TypeError('b²一定要大于等于4ac')
	else:
	    x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
	    x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
	    return x1,x2

print(quadratic(2,3,1))
print(quadratic(1,3,-4))
print(quadratic(0,3,2))
print(quadratic(0,0,1))
print(quadratic(2,4,3))