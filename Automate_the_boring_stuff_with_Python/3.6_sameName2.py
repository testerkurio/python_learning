def spam():
	global eggs
	eggs = 'spam'
spam()
eggs = 'global'
spam()
print(eggs)