'''循环'''

'''for...in循环'''
#打印元素
names = ['Michael','Bob','Tracy']
for name in names:
	print(name)

#计算1-10的整数之和
sum = 0
for x in[1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)

print(list(range(5)))

#生成0-100的整数序列
sum = 0
for x in range(101):
	sum = sum + x
print(sum)

'''while循环'''
#计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
	sum =sum + n
	n = n - 2
print(sum)


'''习题'''

L = ['Bart','Lisa','Adam']
i = 0
while i < 3:
	print('Hello, %s!'%L[i])
	i = i + 1