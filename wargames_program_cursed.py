from random import randint
from time import sleep
import curses
import sys

#
#War Operation Plan Response
#

#Disable Output Buffering
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

#Print tic-tac-toe board & score
def printboard(board):
	global stdscr
	global owin,xwin,nwin
	global sleepcounter
	stdscr.clear()
	stdscr.addch((curses.LINES//2)-9,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-9,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-8,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-8,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-7,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-7,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-6,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-6,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-5,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-5,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-3,curses.ACS_SSSS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2),curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+3,curses.ACS_SSSS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-3,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2),(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+1,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-3,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2),(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+1,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-3,curses.ACS_SSSS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2),curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+3,curses.ACS_SSSS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+3,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+4,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+5,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+6,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+7,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+3,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+4,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+5,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+6,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+7,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addstr((curses.LINES)-1,(curses.COLS//2)-((len("{0} │ {1} │ {2}".format(owin,xwin,nwin)))//2),"{0} | {1} | {2}".format(owin,xwin,nwin))
	for row in range(len(board)):
		cols=[]
		for col in board[row]:
			cols.append(col)
		for col in range(len(cols)):
			if cols[col]=='|O|':
				stdscr.addstr(((curses.LINES//2)-9)+(row*6),((curses.COLS//2)-8)+(col*6),"╭───╮")
				stdscr.addstr(((curses.LINES//2)-8)+(row*6),((curses.COLS//2)-8)+(col*6),"│   │")
				stdscr.addstr(((curses.LINES//2)-7)+(row*6),((curses.COLS//2)-8)+(col*6),"│   │")
				stdscr.addstr(((curses.LINES//2)-6)+(row*6),((curses.COLS//2)-8)+(col*6),"│   │")
				stdscr.addstr(((curses.LINES//2)-5)+(row*6),((curses.COLS//2)-8)+(col*6),"╰───╯")
			elif cols[col]=="|X|":
				stdscr.addstr(((curses.LINES//2)-9)+(row*6),((curses.COLS//2)-8)+(col*6),"╲   ╱")
				stdscr.addstr(((curses.LINES//2)-8)+(row*6),((curses.COLS//2)-8)+(col*6)," ╲ ╱ ")
				stdscr.addstr(((curses.LINES//2)-7)+(row*6),((curses.COLS//2)-8)+(col*6),"  ╳  ")
				stdscr.addstr(((curses.LINES//2)-6)+(row*6),((curses.COLS//2)-8)+(col*6)," ╱ ╲ ")
				stdscr.addstr(((curses.LINES//2)-5)+(row*6),((curses.COLS//2)-8)+(col*6),"╱   ╲")
			else:
				stdscr.addstr(((curses.LINES//2)-9)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-8)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-7)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-6)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
				stdscr.addstr(((curses.LINES//2)-5)+(row*6),((curses.COLS//2)-8)+(col*6),"     ")
	stdscr.refresh()
	sleep(sleepcounter/4)
#Check to see if either player won
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
#Print the gameboard for each player and place a token.
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
#Game set-up and winner announcement
def start_up():
	global owin,xwin,nwin
	global board
	global winner
	global stdscr
	global sleepcounter
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
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-7,"╭")
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2),curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+7,"╮")
		stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)-7,curses.ACS_SBSB)
		stdscr.addstr((curses.LINES//2)-1,(curses.COLS//2)-6," WINNER:  {0}  ".format(winner))
		stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)+7,curses.ACS_SBSB)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-7,"╰")
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2),curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+7,"╯")
		owin=owin+1
		stdscr.refresh()
	elif winner=='X':
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-7,"╭")
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2),curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+7,"╮")
		stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)-7,curses.ACS_SBSB)
		stdscr.addstr((curses.LINES//2)-1,(curses.COLS//2)-6," WINNER:  {0}  ".format(winner))
		stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)+7,curses.ACS_SBSB)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-7,"╰")
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2),curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+7,"╯")
		xwin=xwin+1
		stdscr.refresh()
	else:
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-7,"╭")
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2),curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+7,"╮")
		stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)-7,curses.ACS_SBSB)
		stdscr.addstr((curses.LINES//2)-1,(curses.COLS//2)-6," WINNER: {0}".format(winner))
		stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)+7,curses.ACS_SBSB)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-7,"╰")
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)-1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2),curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+1,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+2,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+3,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+4,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+5,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+6,curses.ACS_BSBS)
		stdscr.addch((curses.LINES//2),(curses.COLS//2)+7,"╯")
		nwin=nwin+1
		stdscr.refresh()
	sleep(sleepcounter*2)
	sleepcounter=sleepcounter*0.99
	return
#Initial dialogue and set-up
if __name__=="__main__":
	sys.stdout= Unbuffered(sys.stdout)
	global stdscr
	global owin,xwin,nwin
	global sleepcounter
	sleepcounter=float(2)
	stdscr=curses.initscr()
	curses.noecho()
	curses.cbreak()
	owin=0
	xwin=0
	nwin=0
	screenstart=0
	stdscr.clear()
	stdscr.move(screenstart,0)
	for each in "GREETINGS PROFESSOR FALKEN.":
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	stdscr.move(screenstart+2,0)
	curses.echo()
	curses.nocbreak()
	stdscr.refresh()
	testinput=input()
	for each in testinput:
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	sleep(1)
	curses.noecho()
	curses.cbreak()
	stdscr.move(screenstart+4,0)
	for each in "HOW ARE YOU FEELING TODAY?":
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	stdscr.move(screenstart+6,0)
	curses.echo()
	curses.nocbreak()
	stdscr.refresh()
	testinput=input()
	for each in testinput:
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	sleep(1)
	curses.noecho()
	curses.cbreak()
	stdscr.move(screenstart+8,0)
	for each in "EXCELLENT. IT'S BEEN A LONG TIME. CAN YOU EXPLAIN THE REMOVAL OF YOUR USER ACCOUNT NUMBER ON 6/23/73?":
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	stdscr.move(screenstart+10,0)
	curses.echo()
	curses.nocbreak()
	stdscr.refresh()
	testinput=input()
	for each in testinput:
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	sleep(1)
	curses.noecho()
	curses.cbreak()
	stdscr.move(screenstart+12,0)
	for each in "YES THEY DO. SHALL WE PLAY A GAME?":
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	stdscr.move(screenstart+14,0)
	curses.echo()
	curses.nocbreak()
	stdscr.refresh()
	testinput=input()
	for each in testinput:
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	sleep(1)
	curses.noecho()
	curses.cbreak()
	sleep(1)
	curses.noecho()
	curses.cbreak()
	stdscr.move(screenstart+16,0)
	for each in "ONE OR TWO PLAYERS?":
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	stdscr.move(screenstart+17,0)
	for each in "PLEASE LIST NUMBER OF PLAYERS:":
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.05)
	curses.echo()
	curses.nocbreak()
	stdscr.refresh()
	testinput=input()
	for each in testinput:
		stdscr.addstr(each)
		stdscr.refresh()
		sleep(0.075)
	sleep(1)
	curses.curs_set(0)
	curses.noecho()
	curses.cbreak()
	stdscr.clear()
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-3,curses.ACS_SSSS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+3,curses.ACS_SSSS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-3,curses.ACS_SSSS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+3,curses.ACS_SSSS)
	stdscr.refresh()
	sleep(0.1)
	stdscr.addch((curses.LINES//2)-5,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-5,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-3,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-3,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+1,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+1,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+2,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+4,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+3,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+3,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.refresh()
	sleep(0.1)
	stdscr.addch((curses.LINES//2)-6,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-6,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-2,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2),(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2),(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+5,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+1,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+4,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+4,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.refresh()
	sleep(0.1)
	stdscr.addch((curses.LINES//2)-7,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-7,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2),curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-1,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2),curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+6,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+5,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+5,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.refresh()
	sleep(0.1)
	stdscr.addch((curses.LINES//2)-8,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-8,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+7,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+6,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+6,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.refresh()
	sleep(0.1)
	stdscr.addch((curses.LINES//2)-9,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-9,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)-8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)-4,(curses.COLS//2)+8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)-8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+2,(curses.COLS//2)+8,curses.ACS_BSBS)
	stdscr.addch((curses.LINES//2)+7,(curses.COLS//2)-3,curses.ACS_SBSB)
	stdscr.addch((curses.LINES//2)+7,(curses.COLS//2)+3,curses.ACS_SBSB)
	stdscr.refresh()
#Repeat game until arbitrary limit reached, then closing dialogue
while __name__=="__main__":
	try:
		global xwin,owin,nwin
		start_up()
		if nwin>randint(randint(randint(500,1500),randint(9000,15000)),500000):
			raise KeyboardInterrupt
	except KeyboardInterrupt or ValueError:
		sleep(0.1)
		stdscr.clear()
		sleep(15)
		curses.curs_set(1)
		stdscr.move(0,0)
		for each in "GREETINGS PROFESSOR FALKEN":
			stdscr.addstr(each)
			stdscr.refresh()
			sleep(0.05)
		stdscr.move(2,0)
		curses.echo()
		curses.nocbreak()
		stdscr.refresh()
		testinput=input()
		for each in testinput:
			stdscr.addstr(each)
			stdscr.refresh()
			sleep(0.05)
		sleep(1)
		curses.noecho()
		curses.cbreak()
		stdscr.move(4,0)
		for each in "A STRANGE GAME.":
			stdscr.addstr(each)
			stdscr.refresh()
			sleep(0.05)
		sleep(1)
		stdscr.move(5,0)
		for each in "THE ONLY WINNING MOVE IS NOT TO PLAY.":
			stdscr.addstr(each)
			stdscr.refresh()
			sleep(0.05)
		sleep(2)
		stdscr.move(7,0)
		for each in "HOW ABOUT A NICE GAME OF CHESS?":
			stdscr.addstr(each)
			stdscr.refresh()
			sleep(0.05)
		sleep(60)
		stdscr.clear()
		stdscr.refresh()
		curses.nocbreak()
		curses.echo()
		curses.endwin()
		exit()
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
		exit()
