'''sorted()'''

#sorted()函数可以对list进行排序
print(sorted([36,5,-12,9,-21]))

#sorted()函数还可以接收一个key函数来实现自定义的排序
#例如按绝对值大小排序
print(sorted([36,5,-12,9,-21],key=abs))

#字符串排序，忽略大小写
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
#反向排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))

'''用sorted()排序的关键在于实现一个映射函数'''


'''习题1'''
#用sorted()对L表分别按名字排序
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
	return t[0].lower() #t为L中的每一项元素，t[0]为元素中的名字

L2 = sorted(L,key = by_name)
print(L2)

'''习题2'''
#用sorted()对L表分别按成绩从高到低排序
def by_score(t):
	return t[1]
L2 = sorted(L,key = by_score,reverse = True)
print(L2)