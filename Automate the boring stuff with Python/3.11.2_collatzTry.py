def collatz(number):
	if (number%2) == 0:
		print(number//2)
		return(number//2)
	else:
		print(3*number+1)
		return(3*number+1)

#将while循环也包含在try里面，这样有错误就不运行while循环了，直接跳出
try:
	number = int(input('Enter number: \n'))
	while True:
		number = collatz(number)
		if number == 1:
			break
except ValueError:
	print('You must enter a int number.')