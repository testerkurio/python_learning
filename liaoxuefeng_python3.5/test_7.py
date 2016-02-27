'''dict'''

d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

print(d)

#通过in判断key是否存在
print('Tomas' in d)

#通过dict提供的get方法
print(d.get('kurio'))
print(d.get('kurio',-1)) #不存在时返回自己指定的value

#删除一个key，对应的value也会删除
d.pop('Bob')
print(d)


'''set'''

s = set([1,2,3]) #提供一个list作为输入集合
print(s)

#重复元素会自动被过滤
s = set([1,1,2,2,3,3,4])
print(s)

#添加元素到set中
s.add(5)
print(s)

#删除元素
s.remove(4)
print(s)

#交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)


'''再议不可变对象'''

#list变化
a = ['c','b','a']
a.sort()
print(a)

#str变化
a = 'abc'
a.replace('a','A')
print(a)

b = a.replace('a','A')
print(b,a)