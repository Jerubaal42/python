from random import randint
from time import sleep
import curses
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
	global stdscr
	global owin,xwin,nwin
	stdscr.clear()
	stdscr.addstr((curses.LINES//2)-9,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)-8,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)-7,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)-6,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)-5,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)-4,(curses.COLS//2)-8,"-----+-----+-----")
	stdscr.addstr((curses.LINES//2)-3,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)-2,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)-1,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2),(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)+1,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)+2,(curses.COLS//2)-8,"-----+-----+-----")
	stdscr.addstr((curses.LINES//2)+3,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)+4,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)+5,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)+6,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES//2)+7,(curses.COLS//2)-3,"|     |")
	stdscr.addstr((curses.LINES)-1,(curses.COLS//2)-((len("{0} | {1} | {2}".format(owin,xwin,nwin)))//2),"{0} | {1} | {2}".format(owin,xwin,nwin))
	for row in range(len(board)):
		cols=[]
		for col in board[row]:
			cols.append(col)
		for col in range(len(cols)):
			if cols[col]=='|O|':
				stdscr.addstr(((curses.LINES//2)-9)+(row*6),((curses.COLS//2)-8)+(col*6),"/---\\")
				stdscr.addstr(((curses.LINES//2)-8)+(row*6),((curses.COLS//2)-8)+(col*6),"|   |")
				stdscr.addstr(((curses.LINES//2)-7)+(row*6),((curses.COLS//2)-8)+(col*6),"|   |")
				stdscr.addstr(((curses.LINES//2)-6)+(row*6),((curses.COLS//2)-8)+(col*6),"|   |")
				stdscr.addstr(((curses.LINES//2)-5)+(row*6),((curses.COLS//2)-8)+(col*6),"\\---/")
			elif cols[col]=="|X|":
				stdscr.addstr(((curses.LINES//2)-9)+(row*6),((curses.COLS//2)-8)+(col*6),"\\   /")
				stdscr.addstr(((curses.LINES//2)-8)+(row*6),((curses.COLS//2)-8)+(col*6)," \\ /  ")
				stdscr.addstr(((curses.LINES//2)-7)+(row*6),((curses.COLS//2)-8)+(col*6),"  X  ")
				stdscr.addstr(((curses.LINES//2)-6)+(row*6),((curses.COLS//2)-8)+(col*6)," / \\ ")
				stdscr.addstr(((curses.LINES//2)-5)+(row*6),((curses.COLS//2)-8)+(col*6),"/   \\")
			else:
				stdscr.addstr(((curses.LINES//2)-9)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-8)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-7)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-6)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-5)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
	stdscr.refresh()
	sleep(0.25)
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
	global stdscr
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
		stdscr.addstr((curses.LINES//2)-2,(curses.COLS//2)-7,"/-------------\\")
		stdscr.addstr((curses.LINES//2)-1,(curses.COLS//2)-7,"| WINNER: {0}   |".format(winner))
		stdscr.addstr((curses.LINES//2),(curses.COLS//2)-7,"\\-------------/")
		owin=owin+1
		stdscr.refresh()
	elif winner=='X':
		stdscr.addstr((curses.LINES//2)-2,(curses.COLS//2)-7,"/-------------\\")
		stdscr.addstr((curses.LINES//2)-1,(curses.COLS//2)-7,"| WINNER: {0}   |".format(winner))
		stdscr.addstr((curses.LINES//2),(curses.COLS//2)-7,"\\-------------/")
		xwin=xwin+1
		stdscr.refresh()
	else:
		stdscr.addstr((curses.LINES//2)-2,(curses.COLS//2)-7,"/-------------\\")
		stdscr.addstr((curses.LINES//2)-1,(curses.COLS//2)-7,"| WINNER:{0} |".format(winner))
		stdscr.addstr((curses.LINES//2),(curses.COLS//2)-7,"\\-------------/")
		nwin=nwin+1
		stdscr.refresh()
	sleep(1)
	return
if __name__=="__main__":
	sys.stdout= Unbuffered(sys.stdout)
	global stdscr
	global owin,xwin,nwin
	stdscr=curses.initscr()
	curses.noecho()
	curses.cbreak()
	owin=0
	xwin=0
	nwin=0

while __name__=="__main__":
	try:
		start_up()
		if nwin>50:
			raise ValueError
	except KeyboardInterrupt or ValueError:
		sleep(0.1)
		stdscr.clear()
		stdscr.move((curses.LINES//2),(curses.COLS//2)-10)
		for each in "War is a Strange Game":
			stdscr.addstr(each)
			stdscr.refresh()
			sleep(0.075)
		sleep(1)
		stdscr.move((curses.LINES//2)+1,(curses.COLS//2)-18)
		for each in "The Only Winning Move is Not to Play":
			stdscr.addstr(each)
			stdscr.refresh()
			sleep(0.075)
		sleep(1)
		curses.nocbreak()
		curses.echo()
		curses.endwin()
	except:
		sleep(0.1)
		stdscr.clear()
		stdscr.addstr(0,0,"If you are seeing this message, the screen is probably too small for the program.")
		stdscr.refresh()
		sleep(5)
		curses.nocbreak()
		curses.echo()
		curses.endwin()
		raise
	finally:
		exit()
