catNames = []
while True:
	# len(catNames)+1 用于累加，提示输入下一只猫的名字
	print('Enter the name of cat ' + str(len(catNames)+1) + ' (Or enter noting to stop.):')
	name = input()
	if name == '':
		break
	catNames = catNames + [name] #list concatenation
print('The cat names are:')
for name in catNames:
	print(' ' + name)