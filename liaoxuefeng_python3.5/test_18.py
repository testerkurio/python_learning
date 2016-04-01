'''map/reduce'''

'''map()函数'''

#map()函数接收两个参数，一个是函数，一个是Iterable
#map将传入的函数依次作用到序列的每个元素，并将结果作为新的Iterator返回

#f(x)=x*x
def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

'''reduce()函数'''

#reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积运算，如reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)

#对序列求和
from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))

#reduce()还可以接收第3个可选参数，作为计算的初始值
print(reduce(add,[1,3,5,7,9],100))

#将序列[1,3,5,7,9]变换为整数13579
from functools import reduce
def fn(x,y):
	return x*10 + y
print(reduce(fn,[1,3,5,7,9]))

#配合map()，把str转换为int
from functools import reduce
def fn(x,y):
	return x*10 + y
def char2num(s):
	'''把前面看作名为D的dict，即返回D[s]，就是返回dict中s参数对应的value'''
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(fn,map(char2num,'13579')))
print(char2num('2'))

#整理成一个str2int函数
from functools import reduce
def str2int(s):
	def fn(x,y):
		return x*10 +y
	def char3num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))

#用lambda函数进一步简化
from functools import reduce
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))


'''习题1'''
#将输入的名称变为首字母大写，其他小写
def normalize(name):
	return name[0].upper()+name[1:].lower()

L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)

'''习题2'''
#接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print('3*5*7*9 =',prod([3,5,7,9]))

#还可以用lambda函数简化
from functools import reduce
def prod(L):
	return reduce(lambda x,y:x*y,L)
print('3*5*7*9 =',prod([3,5,7,9]))

'''习题3'''
#利用map和reduce编写str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2floatGt0(s):
    return reduce(lambda x,y: x*10 + y, map(char2num,s))

def str2floatLt0(s):
    return (reduce(lambda x,y: 0.1*x + y, map(char2num, s[::-1]))/10)

def str2float(s):
    pointIndex = s.index('.')
    return str2floatGt0(s[:pointIndex]) + str2floatLt0(s[(pointIndex+1):])

print('str2float(\'123.456\') =',str2float('123.456'))


'''直接使用float()函数'''
print(float('123.456'))