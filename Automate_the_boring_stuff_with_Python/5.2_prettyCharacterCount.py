import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1

pprint.pprint(count)
#与上面的表达式是等价的
#print(pprint.pformat(count))