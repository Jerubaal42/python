from random import randint
from time import sleep
def printboard(board):
	for row in range(len(board)):
		for col in board[row]:
			if col=='|o|':
				print("\033[1;92;40m",col, end="")
			elif col=="|x|":
				print("\033[1;91;40m",col,end="")
			else:
				print("\033[1;97;40m",col,end="")
		print("\033[0;97;40m",end="\n")
		sleep(0.1)
	print(end="\n")
	sleep(0.1)
def winchecker(board,player):
	global winner
	losegame=[]
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[c][r]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			return(player)
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[r][c]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			return(player)
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[r][r]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			return(player)
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[r][len(board)-(1+r)]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			return(player)
	for r in range(len(board)):
		if '| |'  in board[r]:
			pass
		else:
			losegame.append('lose')
	if len(losegame)==len(board) and winner=='':
		return('Nobody')
def playgame(board,playersym):
	while True:
		for player in playersym:
			printboard(board)
			while True:
				row=(int(randint(1,3)))
				col=(int(randint(1,3)))
				if board[row-1][col-1]!='| |':
					continue
				else:
					break
			board[row-1][col-1]='|{0}|'.format(player)
			if winchecker(board,player)!=None:
				return(winchecker(board,player))
def start_up():
	global board
	global winner
	winner=''
	board=[]
	playersym=['o','x']
	players=2
	boardsize=3
	for x in range(0,boardsize):
		board.append(['| |']*boardsize)
	winner=playgame(board,playersym)
	printboard(board)
	if winner=='o':
		print("\033[1;92;40m{0} wins!".format(winner))
	elif winner=='x':
		print("\033[1;91;40m{0} wins!".format(winner))
	else:
		print("\033[1;97;40m{0} wins!".format(winner))
	sleep(0.1)
	print("\033[0;97;40m")
	sleep(0.5)
	return
while __name__=="__main__":
	try:
		start_up()
	except:
		print('\n\033[1;91;40mThe Only Winning Move is Not to Play\033[0;97;40m')
		exit()
