message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
	#设立key
	count.setdefault(character,0)
	#count[character]为该key的值
	count[character] = count[character] + 1

print(count)