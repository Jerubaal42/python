import tkinter as tk
from random import randint
import turtle 

LARGE_FONT= ("Verdana", 12)

#Menus
class initialize(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		tk.Tk.wm_title(self,"Menu")

		container.pack(side="top",fill="both",expand = True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartMenu,MineSetup,Minesweeper):
			frame = F(container,self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		self.show_frame(StartMenu)

	def show_frame(self, cont):
		frame=self.frames[cont]
		frame.tkraise()
        
class StartMenu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		button=tk.Button(self, text="Minesweeper",command=lambda: controller.show_frame(MineSetup))
		button.pack()

		button=tk.Button(self, text="Damian Pic",command=damian)
		button.pack()
		
		button=tk.Button(self, text="Shaeden Pic",command=shaeden)
		button.pack()

		button=tk.Button(self,text="Exit",command=b_exit)
		button.pack()
		
class MineSetup(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		global msret
		global mscet
		global msmet

		msret=tk.IntVar()
		mscet=tk.IntVar()
		msmet=tk.IntVar()

		msrl=tk.Label(self,text="Rows:")
		msrl.pack(side="top")
	
		msre=tk.Entry(self,textvariable=msret)
		msre.pack(side="top")
        
		mscl=tk.Label(self,text="Columns:")
		mscl.pack(side="top")
        
		msce=tk.Entry(self,textvariable=mscet)
		msce.pack(side="top")
		
		msml=tk.Label(self,text="Mines:")
		msml.pack(side="top")
		
		msme=tk.Entry(self,textvariable=msmet)
		msme.pack(side="top")
		
		mssb=tk.Button(self,text="Submit",command=Minesweeper.m_setup)
		mssb.pack(side="top")
		
		mseb=tk.Button(self,text="Exit",command=b_exit)
		mseb.pack(side="bottom")

class Minesweeper(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
	def m_setup():

		minesweeper=tk.Toplevel()
		minesweeper.wm_title("Minesweeper")

		global board_row
		global board_col
		global mines
		global board
		global not_dead
		global b
		def m_random_row(board):
			return randint(0,len(board)-1)
		def m_random_col(board):
			return randint(0,len(board)-1)
		def m_create_board():
			for x in range(0,board_col):
				board.append([' ']*board_row)
		def m_mine_repeat():
			mine_row=m_random_row(board)
			mine_col=m_random_col(board)
			if [mine_row,mine_col] in mines:
				m_mine_repeat()
			else:
				mines.append([mine_row,mine_col])
		def m_game_end():
			rp=tk.Button(minesweeper,text="Play Again?")
			rp.grid(columnspan=board_row)
		def m_blank_count():
			blank_count=0
			for x in range(0,board_row):
				for y in range(0,board_col):
					if board[x][y]==' ':
						blank_count=blank_count+1
			return blank_count
		not_dead=bool(True)
		board=[]
		mines=[]
		board_row=int(msret.get())
		board_col=int(mscet.get())
		m_create_board()
		mine_number=int(msmet.get())
		if mine_number>board_row*board_col:
			raise ValueError
		for mine in range (0,mine_number):
			mine_row=m_random_row(board)
			mine_col=m_random_col(board)
			if [mine_row,mine_col] in mines:
				m_mine_repeat()
			else:
				mines.append([mine_row,mine_col])
		for r in range(0,board_row):
			for c in range(0,board_col):
				b=tk.Button(minesweeper,text=board[r][c],width=1,height=1)
				b.grid(row=r,column=c)
				b['command']=command=lambda r=r,c=c,b=b: m_button_press(r,c,b)
		def m_button_press(r,c,b):
			m_bang(r,c,b)
			b.config(state='disabled',relief='sunken',text=board[r][c])
		def m_bang(x,y,b):
			m_check_mines(x,y)
			if [x,y] in mines:
				m_game_end()
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
def b_exit():
	exit()
	
def damian():
	
	Canvas=turtle.Screen()
	Canvas.bgcolor("black")
	Canvas.title("Damian's Turtle")

	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 0, 0)
	turtle.hideturtle()
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)
	turtle.speed(4.5)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 58, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 108, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 161, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(208, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(115, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)

	 
	 
	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(117, 254, 147)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(0, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(106, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(163, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 0, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)




	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 58, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 108, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 161, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(208, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(115, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)

	 
	 
	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(117, 254, 147)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(0, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(106, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(163, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 0, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)




	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 58, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 108, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 161, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(208, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(115, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)

	 
	 
	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(117, 254, 147)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(0, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(106, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(163, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 0, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)




	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 58, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 108, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 161, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(208, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(115, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)

	 
	 
	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(117, 254, 147)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(0, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(106, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(163, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 0, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)




	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 58, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 108, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 161, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(208, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(115, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)

	 
	 
	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(117, 254, 147)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(0, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(106, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(163, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 0, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)




	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 58, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 108, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(255, 161, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(208, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(115, 254, 0)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)

	 
	 
	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(117, 254, 147)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(0, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(106, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	turtle.shape("square")
	turtle.colormode(255)
	turtle.color(163, 0, 255)
	turtle.forward(150)
	turtle.left(85)
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(150)
	turtle.left(23)
	turtle.forward(100)
	turtle.left(60)



	input("Press enter to end")

	win.close()

	#cut off point
def shaeden():

	Canvas=turtle.Screen()
	Canvas.bgcolor("black")
	Canvas.title("Shaeden's Turtle")

	turtle.color("green")
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	turtle.speed(50)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.color("yellow")
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	turtle.color("red")
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.left(5)
	
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	
	turtle.speed(50)





app = initialize()
app.mainloop()
