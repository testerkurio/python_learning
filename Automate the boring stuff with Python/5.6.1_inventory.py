stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
	print('Inventory:')
	item_number = 0
	for k,v in inventory.items():
		print(str(v) + ' ' + k)
		item_number += v
	print('Total number of items:' + str(item_number))

displayInventory(stuff)