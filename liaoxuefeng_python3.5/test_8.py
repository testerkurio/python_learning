'''调用内置函数'''

#绝对值函数abs()
print(abs(100))
print(abs(-20))
print(abs(12.34))

#返回最大值函数max()
print(max(1,2))
print(max(2,3,1,-7))


'''数据类型转换'''

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

#将函数名附给一个变量
a = abs
print(a(-23))


'''习题'''

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))