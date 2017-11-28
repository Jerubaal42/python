from random import randint
from time import sleep
import sys

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

def printboard(board):
	for row in range(len(board)):
		for col in board[row]:
			if col=='|O|':
				print("\033[1;92;40m",col, end="")
			elif col=="|X|":
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
		return('NONE')
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
	global owin,xwin,nwin
	global board
	global winner
	winner=''
	board=[]
	playersym=['O','X']
	players=2
	boardsize=3
	for x in range(0,boardsize):
		board.append(['| |']*boardsize)
	winner=playgame(board,playersym)
	printboard(board)
	if winner=='O':
		print(" \033[1;92;40mWINNER: {0}\033[0;97;40m".format(winner))
		owin=owin+1
	elif winner=='X':
		print(" \033[1;91;40mWINNER: {0}\033[0;97;40m".format(winner))
		xwin=xwin+1
	else:
		print(" \033[1;97;40mWINNER: {0}\033[0;97;40m".format(winner))
		nwin=nwin+1
	sleep(0.1)
	print("")
	sleep(0.1)
	print(" \033[1;92;40m{0} \033[1;97;40m| \033[1;91;40m{1} \033[1;97;40m| {2}\033[0;97;40m".format(owin,xwin,nwin))
	sleep(0.1)
	print("")
	sleep(0.5)
	print("")
	sleep(0.1)
	return
if __name__=="__main__":
	sys.stdout= Unbuffered(sys.stdout)
	global owin,xwin,nwin
	owin=0
	xwin=0
	nwin=0

while __name__=="__main__":
	try:
		start_up()
		if nwin>50:
			raise ValueError
	except:
		sleep(0.1)
		print('\n \033[1;91;40m',end="")
		for each in "War is a Strange Game":
			print(each,end="")
			sleep(0.075)
		print('\033[0;97;40m\n')
		sleep(1)
		print(' \033[1;91;40m',end="")
		for each in "The Only Winning Move is Not to Play":
			print(each,end="")
			sleep(0.075)
		print('\033[0;97;40m\n')
		sleep(1)
		exit()
