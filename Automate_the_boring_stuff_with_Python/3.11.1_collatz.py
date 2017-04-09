#定义一个函数
def collatz(number):
	if (number%2) == 0: #验证number是否为偶数
		print(number//2)
		return(number//2)
	else:
		print(number*3+1)
		return(number*3+1)

number = int(input('Enter number: \n'))

while True: #重复循环，用于不停调用collatz()函数
	number = collatz(number) #将返回值重新赋值给number
	if number == 1:
		break