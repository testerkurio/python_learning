'''条件判断'''

#只有if
age = 20
if age >= 18:
	print('your age is',age)
	print('adult')

#加上else
age = 3
if age >= 18:
	print('your age is',age)
	print('adult')
else:
	print('your age is',age)
	print('teenager')

#用elif
age = 3
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

#从上往下判断，若为true，则忽略剩下内容
age = 20
if age >= 6:
	print('teenager')
elif age >= 18:
	print('adult')
else:
	print('kid')

#简写
if 1:
	print('True')


'''再议input'''
'''
birth = int(input('birth: '))
if birth < 2000:
	print('00前')
else:
	print('00后')
'''

'''习题'''

hight = float(input('what\'s your hight?(m)\n'))
wight = float(input('what\'s your wight?(kg)\n'))
BMI = wight/(hight*hight)
if BMI < 18.5:
	print('you are too light!')
elif BMI >= 18.5 and BMI <= 25:
	print('you are normal.')
elif BMI > 25 and BMI <= 28:
	print('you are overweight.')
elif BMI > 28 and BMI <= 32:
	print('you are fat.')
elif BMI > 32:
	print('you are heavy fat!')
print('your BMI are: %.2f'%BMI) #取两位小数