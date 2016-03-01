'''迭代器'''

'''可直接作用于for循环的数据类型：
1.集合数据类型：list、tuple、dict、set、str等
2.generator，包括生成器和带yield的generator function
这些可直接作用于for循环的对象统称为可迭代对象：Iterable'''

'''可用isinstance()判断一个对象是否是Iterable对象'''

from collections import Iterable
print(isinstance([],Iterable)) #list
print(isinstance({},Iterable)) #tuple
print(isinstance('abx',Iterable)) #str
print(isinstance((x for x in range(10)),Iterable)) #生成器
print(isinstance(100,Iterable)) #整数

