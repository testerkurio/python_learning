'''迭代'''

#如果给定一个list或tuple，用for循环遍历，称为迭代
#使用for...in完成迭代

'''迭代dict'''
d = {'a':1,'b':2,'c':3}

#dict默认迭代key
for key in d:
	print(key)

#迭代value
for value in d.values():
	print(value)

#同时迭代key和value
for k,v in d.items():
	print(k,v)

'''迭代字符串'''
for ch in 'ABC':
	print(ch)

'''判断对象是否为可迭代对象'''
from collections import Iterable
print(isinstance('abc',Iterable)) #判断str是否可迭代
print(isinstance([1,2,3],Iterable)) #判断list是否可迭代
print(isinstance(123,Iterable)) #判断整数是否可迭代

'''对list实现类似java那样的下表循环'''
#使用内置的enumerate()函数，可将list变成索引-元素对
for i,value in enumerate(['A','B','C']):
	print(i,value)