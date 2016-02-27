'''高级特性'''

'''切片'''

#取指定索引范围的list或tuple中的部分元素
L = ['Michael','Sarah','Tracy','Bob','Jack']

#笨方法,取前3个元素
print([L[0],L[1],L[2]]) #不适合取N个元素

#使用循环，取前3个元素
r = []
n = 3
for i in range(n):
	r.append(L[i])

print(r) #循环十分繁琐

#切片操作
print(L[0:3]) #从0开始到3为止，不包括索引3
print(L[:3]) #如果第一个索引为0，还可以省略
print(L[-2:]) #也支持倒数切片
print(L[-2:-1]) #倒数第一个元素的索引是-1

#创建一个0-99的列表
L = list(range(100))
print(L)

print(L[:10]) #前10个
print(L[-10:]) #后10个
print(L[10:20]) #前11-20个
print(L[:10:2]) #前10个，每两个取一个
print(L[::5]) #所有数，每5个取一个
print(L[:]) #原样复制一个list

#tuple也可以用切片操作，结果仍是tuple
T = tuple(range(10))
print(T)
print(T[:3])

#字符串也可以用切片操作，只是结果仍是字符串
print('abcdefg'[:3])
print('abcdefg'[::2])