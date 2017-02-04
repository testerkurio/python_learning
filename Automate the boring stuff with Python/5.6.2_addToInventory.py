# 按照格式打印物品列表，并统计物品总数量
def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k,v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print('Total number of items: ' + str(item_total))

# 加入打怪爆出的物品，并更新到字典中
def addToInventory(inventory, addedItems):
	# 将列表中的每一项对应到字典的键，然后将对应的value值累加1
	for i in addedItems:
		inventory.setdefault(i,0)
		inventory[i] = inventory[i] + 1
	# 返回累加过value值的字典
	return inventory

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)