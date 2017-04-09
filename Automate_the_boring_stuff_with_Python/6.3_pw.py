#! python3
# 6.3_pw.py - An insecure password locker program.

PASSWORDS = {'email': 'kuriollr@163.com', 'blog': 'kurio', 'luggage': 'qwertyu89l'}


import sys, pyperclip

#sys.argv列表中第一项为字符串(包含文件名称)，第二项为命令行参数，是必须要有的
if len(sys.argv) < 2:
	print('Usage: python 6.3_pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)