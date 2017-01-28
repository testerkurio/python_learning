
spam = ['apples','bananas','tofu','cats']
fruit = ['purple','lean','peach','cherry']

def printcopy(lists):
	for i in range(0,len(lists)):
		print(lists[i]+', ',end='') #去除尾部的自动换行
		if i == len(lists)-1:
			print('and '+lists[i])

printcopy(spam)
printcopy(fruit)