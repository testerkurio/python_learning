'''filter()函数'''
#用于过滤序列，也接收一个函数和一个序列
#与map()不同的是，filter()根据返回值是true还是false决定保留还是丢弃该元素

#例：一个list，删掉偶数，只保留奇数
def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,9,10,15])))

#例：把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'C','  '])))

'''求素数'''
#计算素数的一个方法是埃氏筛法
def _odd_iter():
	n = 1
	while True:
		n = n + 2  #构造一个从3开始的奇数序列
		yield n  #这是一个生成器，并且是一个无限序列

def _not_divisible(n):
	return lambda x: x % n > 0  #定义一个筛选函数

def primes():
	yield 2
	it = _odd_iter() #初始序列
	while True:
		n = next(it) #返回序列的第一个数
		yield n
		it = filter(_not_divisible(n),it) #构造新序列

for n in primes():
	if n < 100:
		print(n)
	else:
		break


'''习题'''
#用filter()函数过滤掉非回数
def is_palindrome(n):
	s = list(str(n))
	return s == s[::-1] and n > 10

output = filter(is_palindrome,range(1,1000))
print(list(output))