'''list'''

classmates = ['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])

#倒数
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

#追加元素到末尾
classmates.append('Adam')
print(classmates)

#把元素插入到指定的位置
classmates.insert(1,'Jack')
print(classmates)

#删除list末尾的元素
classmates.pop()
print(classmates)

#删除指定位置的元素
classmates.pop(1)
print(classmates)

#把某个元素替换成别的元素
classmates[1] = 'Sarah'
print(classmates)


'''tuple'''

#tuple一旦初始化就不能修改
t = (1,2)


'''习题'''

L = [['Apple','Google','Microsoft'],['Java','Python','Ruby','PHP'],['Adam','Bart','Lisa']]
#打印Apple
print(L[0][0])
#打印Python
print(L[1][1])
#打印Lisa
print(L[2][2])