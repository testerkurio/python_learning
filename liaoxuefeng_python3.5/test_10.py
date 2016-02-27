'''位置参数'''

'''
def power(x):
	return x*x #x为一个位置参数
'''
def power(x,n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
#x和n都为位置参数，传入的值按位置顺序依次赋予
print(power(2,5))


'''默认参数'''

def power(x,n=2): #将n默认为2
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5)) #相当于调用power(5,2)

'''
1.必选参数在前，默认参数在后
2.将变化大的参数放前面，变化小的参数放后面作为默认参数
3.默认参数必须指向不变对象
'''
def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city',city)

print(enroll('Sarah','F'))
print(enroll('Bob','M',7))
print(enroll('Adam','M',city='Tianjin'))


'''可变参数'''

'''
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

print(calc([1,2,3]))
print(calc([1,3,5,7]))
'''
#改为可变参数,在参数前加个*号
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

print(calc(1,2))
print(calc())

nums = [3,4,6]
print(calc(*nums)) #将nums这个list的所有元素作为可变参数传进去


'''关键字参数'''

def person(name,age,**kw): #关键字参数kw，自动组装为一个dict
	print('name:',name,'age:',age,'other:',kw)

#关键字参数可以扩展函数的功能
print(person('Michael',30))
print(person('Bob',35,city='Beijing'))
print(person('Adam',45,gender='M',job='Engineer'))

extra = {'city':'Beijing','job':'Engineer'}
print(person('Jack',24,city=extra['city'],job=extra['job']))
#简化的写法
print(person('Jack',24,**extra))


'''命名关键字参数'''

#如果要限制关键字参数的名字，就可以用命名关键字参数
#特殊分隔符*后面的参数被视为命名关键字参数
def people(name,age,*,city,job):
	print(name,age,city,job)

#命名关键字参数必须传入参数名
print(people('Jack',24,city='Beijing',job='Engineer'))


'''参数组合'''

def f1(a,b,c=0,*args,**kw):
	print('a =',a,'b =',b,'c =',c,'args =',args,'kw =',kw)

def f2(a,b,c=0,*,d,**kw):
	print('a =',a,'b =',b,'c =',c,'d =',d,'kw =',kw)

print(f1(1,2))
print(f1(1,2,c=3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x=99))
print(f2(1,2,d=99,ext=None))

args = (1,2,3,4)
kw = {'d':99,'x':'#'}
print(f1(*args,**kw))

args = (1,2,3)
kw = {'d':88,'x':'#'}
print(f2(*args,**kw))


'''小结'''
'''
1.默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误；
2.*args是可变参数，args接收的是一个tuple————不可变列表；
3.**kw是关键字参数，kw接收的是一个dict————有key和value；
4.可变参数可直接传入func(1,2,3),也可先组装list或tuple，再通过*args传入func(*(1,2,3));
5.关键字参数可直接传入func(a=1,b=2)，也可先组装dict，在通过**kw传入func(**{'a':1,'b':2})；