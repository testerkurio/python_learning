allGuests = {'Alice':{'apple':5,'pretzels':12},
			 'Bob':{'ham sandwiches':3,'apples':2},
			 'Carol':{'cups':3,'apple pies':1}}

def totalBrought(guests, item):
	numBrought = 0 #初始化
	for k,v in guests.items(): # v为字典中的字典
		# 遍历列表中的每一项统计item的个数
		numBrought = numBrought + v.get(item,0) # v.get(item,0)为item的个数
	return numBrought

print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests,'apples')))
print(' - Cups ' + str(totalBrought(allGuests,'cups')))
print(' - Cakes ' + str(totalBrought(allGuests,'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests,'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests,'apple pies')))