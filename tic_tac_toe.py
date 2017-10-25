def printboard(board):
	for row in range(len(board)):
		for col in board[row]:
			print(col, end="")
		print(end="\n")
def winchecker(board,player):
	global winner
	global playing
	losegame=[]
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[c][r]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			winner=player
			endgame()
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[r][c]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			winner=player
			endgame()
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[r][r]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			winner=player
			endgame()
	for c in range(len(board)):
		wingame=[]
		for r in range(len(board)):
			if board[r][len(board)-(1+r)]=='|{0}|'.format(player):
				wingame.append('win')
		if len(wingame)==len(board):
			winner=player
			endgame()
	for r in range(len(board)):
		if '| |'  in board[r]:
			pass
		else:
			losegame.append('lose')
	if len(losegame)==len(board) and winner=='':
		winner="Nobody"
		endgame()
def playgame(board,playersym):
	global playing
	playing=True
	while playing==True:
		for player in playersym:
			while True:
				printboard(board)
				print("It is {0}'s turn".format(player))
				while True:
					try:
						row=(int(input("Choose row: ")))
						if row>len(board[0]):
							raise ValueError
						else:
							break
					except:
						print("Invalid Number")
				while True:
					try:
						col=(int(input("Choose column: ")))
						if col>len(board):
							raise ValueError
						else:
							break
					except:
						print("Invalid Number")
				if board[row-1][col-1]!='| |':
					continue
				else:
					break
			board[row-1][col-1]='|{0}|'.format(player)
			winchecker(board,player)
def start_up():
	global board
	board=[]
	playersym=[]
	players=1
	while True:
		try:
			players=int(input("Enter number of players: "))
			if players>62 or players<1:
				raise ValueError
			else:
				break
		except:
			print("Invalid Number")
	while True:
		try:
			boardsize=int(input("Enter board size: "))
			if boardsize<1:
				raise ValueError
			else:
				break
		except:
			print("Invalid Number")
	for x in range(0,boardsize):
		board.append(['| |']*boardsize)
	for p in range(1,players+1):
		while True:
			try:
				setplayersym=str(input("Enter player symbol for player {0}: (one character)".format(p)))
				if setplayersym=="":
					raise ValueError
				elif len(setplayersym)>1:
					raise ValueError
				elif setplayersym in playersym:
					raise ValueError
				else:
					break
			except:
				print("Invalid Symbol")
		playersym.append(setplayersym)
	playgame(board,playersym)
	return board
def endgame():
	global board
	global playing
	global winner
	playing=False
	printboard(board)
	print("{0} wins!".format(winner))
	playagain=input("Would you like to play again?")
	if playagain=="yes" or playagain=="y" or playagain=="ja" or playagain=="si":
		start_up()
	else:
		exit()
if __name__=="__main__":
	start_up()
