'''字符编码'''

print("包含中文的str")

print('ord(A)=',ord('A'))
print('chr(66)=',chr(66))
print('chr(25991)=',chr(25991))


print("显示正常的中文")


'''格式化'''

print('Hello, %s'%'world')
print('Hi, %s, you have $%d.'%('Michael',1000000))

print('%2d-%02d'%(3,1))
print('%.2f'%3.1415926)

print('Age: %s.Gender: %s'%(25,True))
print('growth rate:%d %%'%7)

percent = (85-72)/72*100
print("小明的成绩提升了:%.1f %%"%percent)