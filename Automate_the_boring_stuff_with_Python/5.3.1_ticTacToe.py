theBoard = {'top-L':' ','top-M':' ','top-R':' ',
			'mid-L':' ','mid-M':' ','mid-R':' ',
			'low-L':' ','low-M':' ','low-R':' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9): #默认从0开始，可移动9步
	printBoard(theBoard)
	print('Turn for ' + turn + '. Move on which space?')
	move = input() #输入当前填入的位置
	theBoard[move] = turn #将当前填入位置的值赋予当前的黑子或白子
	if turn == 'X': #转换黑子或白子
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)