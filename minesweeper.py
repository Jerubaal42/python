from random import randint
def m_random_row(board):
	return randint(0,len(board)-1)
def m_random_col(board):
	return randint(0,len(board)-1)
def m_create_board():
	for x in range(0,board_col):
		board.append(['O']*board_row)
def m_print_board(board):
	strlen=""
	strleninit=len(str(board_col))
	strlenupd=0
	for each in range(strleninit):
		strlen+=" "
	print(strlen,end=" ")
	for col in range(board_col):
		if len(str(col+1))+len(strlen)>strleninit:
			strlenupd+=1
			strlen=""
			for each in range(strleninit-strlenupd):
				strlen+=" "
		print(col+1,end=strlen)
	print(end="\n")
	strlen=""
	strleninit=len(str(len(board)))
	strlenupd=0
	for each in range(strleninit):
		strlen+=" "
	for row in range(len(board)):
		if len(str(row+1))+len(strlen)>strleninit:
			strlenupd+=1
			strlen=""
			for each in range(strleninit-strlenupd):
				strlen+=" "
		print(str(row+1)+(strlen),end="|")
		for col in board[row]:
			print(col,end=" ")
		print(end="\n")
def m_mine_repeat():
	mine_row=m_random_row(board)
	mine_col=m_random_col(board)
	if [mine_row,mine_col] in mines:
		m_mine_repeat()
	else:
		mines.append([mine_row,mine_col])
def m_add_mines():
	while True:
		try:
			mine_number=int(input("Number of Mines: "))
			if mine_number>board_row*board_col:
				raise ValueError
		except:
			print("That's not a valid number.")
		else:
			break
	for mine in range (0,mine_number):
		mine_row=m_random_row(board)
		mine_col=m_random_col(board)
		if [mine_row,mine_col] in mines:
			m_mine_repeat()
		else:
			mines.append([mine_row,mine_col])
def m_check_mines(x,y):
	mine_checker=bool(True)
	nearby_mines=0
	for r in range(-1,2):
		for c in range(-1,2):
			if [x+r,y+c] in mines:
				nearby_mines=nearby_mines+1
	if [x,y] in mines:
		board[x][y]='X'
	else:	
		board[x][y]=str(nearby_mines)
	if nearby_mines==0:
		m_check_mines_rec(x,y)
def m_check_mines_rec(x,y):
	for r1 in range(-1,2):
		for c1 in range(-1,2):
			if ((r1+x) < 0 or (r1+x) > (board_row-1)) or ((c1+y) < 0 or (c1+y) > (board_col-1)):
				continue
			elif r1==0 and c1==0:
				continue
			elif board[x+r1][y+c1]=='0':
				continue
			else:
				m_check_mines(x+r1,y+c1)
def m_play_game():
	m_print_board(board)
	while True:
		try:
			guess_row=int(input("Guess Row: "))-1
			guess_col=int(input("Guess Column: "))-1
			if guess_row>board_row or guess_col>board_col:
				raise ValueErrpr
		except:
			print("That's not a valid number.")
		else:
			m_check_mines(guess_row,guess_col)
			if [guess_row,guess_col] in mines:
				print ("BOOM! Game Over")
				not_dead=bool(False)
				m_game_end()
			break
def m_game_end():
	replay=input("Would you like to play again? ")
	if replay=="yes" or replay=="y" or replay=="ja" or replay=="si":
		minesweeper()
	elif replay!="yes" or replay!="y" or replay!="ja" or replay!="si":
		raise SystemExit
def m_blank_count():
	blank_count=0
	for x in range(0,board_row):
		for y in range(0,board_col):
			if board[x][y]=='O':
				blank_count=blank_count+1
	return blank_count
def minesweeper():
	global board_row
	global board_col
	global board
	global mines
	global not_dead
	not_dead=bool(True)
	while True:
		try:
			board_row=int(input("Rows on Board: "))
		except:
			print("Not a valid number.")
		else:
			break
	while True:
		try:
			board_col=int(input("Columns on Board: "))
		except:
			print("Not a valid number.")
		else:
			break
	board=[]
	mines=[]
	m_create_board()
	m_add_mines()
	while not_dead==True:
		if len(mines)>=m_blank_count():
			break
		m_play_game()
	m_print_board(board)
	print('You win!')
	m_game_end()
while True:
	minesweeper()
