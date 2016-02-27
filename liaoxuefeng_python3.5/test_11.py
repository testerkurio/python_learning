'''递归函数'''

'''递归函数的优点就是逻辑简单清晰'''
def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)

print(fact(1))
print(fact(5))

'''print(fact(1000))'''
'''递归调用的次数过多，会导致栈溢出;解决递归调用栈溢出的方法是通过尾递归优化；
尾递归是指，在函数返回的时候调用自身本身，并且return语句不能包含表达式'''

def fact1(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num - 1,num * product)

print(fact(5))
'''print(fact(1000))'''
'''大多数编程语言没有针对尾递归做优化，python解释器也没有，
所以改成尾递归方式还是会导致栈溢出'''


'''习题'''

#汉诺塔的移动问题
def move(n,a,b,c):
	if n == 1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b) #将前n-1个盘子从a移动到b上
		move(1,a,b,c) #将最底下的最后一个盘子从a移动到c上
		move(n-1,b,a,c) #将b上的n-1个盘子移动到c上

print(move(5,'A','B','C'))
''''''
