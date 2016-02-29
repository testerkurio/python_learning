'''列表生成式'''

#要生成从1-10的list，可用list(range(1,11))
print(list(range(1,11)))

#生成[1x1,2x2,3x3,...,10x10]，可用循环
L = []
for x in range(1,11):
	L.append(x * x)
print(L)

#可以用列表生成式
print([x*x for x in range(1,11)])
#要生成的元素x*x放前面，后面跟for循环

#for循环后面还可以加上if判断，筛选仅偶数的平方
print([x*x for x in range(1,11) if x%2 == 0])

#还可使用两层循环，生成全排列
print([m+n for m in 'ABC' for n in 'XYZ'])

#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

#for循环可使用两个或多个变量
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print(k,'=',v)

print([k+'='+v for k,v in d.items()])

#把一个list中所有的字符串变成小写
L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])


'''习题'''

L1 = ['Hello','World',18,'Apple',None]
#isinstance()函数用来判断一个变量是否为字符串
L2 = [s.lower() for s in L1 if isinstance(s,str) == True]
print(L2)