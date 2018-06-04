from random import randint
from time import sleep
import curses

if __name__=="__main__":
	global stdscr
	stdscr=curses.initscr()
	curses.noecho()
	curses.cbreak()
	if (curses.LINES/2).is_integer():
		creditwindowbord=curses.newwin(curses.LINES//2,curses.COLS//2,0,(curses.COLS//2))
		creditwindow=curses.newwin((curses.LINES//2)-2,(curses.COLS//2)-2,1,(curses.COLS//2)+1)
		imagewindowbord=curses.newwin(curses.LINES//2,curses.COLS//2,(curses.LINES//2),(curses.COLS//2))
		imagewindow=curses.newwin((curses.LINES//2)-2,(curses.COLS//2)-2,(curses.LINES//2)+1,(curses.COLS//2)+1)
	else:
		creditwindowbord=curses.newwin((curses.LINES//2)+1,curses.COLS//2,0,(curses.COLS//2))
		creditwindow=curses.newwin((curses.LINES//2)-1,(curses.COLS//2)-2,1,(curses.COLS//2)+1)
		imagewindowbord=curses.newwin(curses.LINES//2,curses.COLS//2,(curses.LINES//2)+1,(curses.COLS//2))
		imagewindow=curses.newwin((curses.LINES//2)-2,(curses.COLS//2)-2,(curses.LINES//2)+2,(curses.COLS//2)+1)
	lyricwindowbord=curses.newwin(curses.LINES,curses.COLS//2,0,0)
	lyricwindow=curses.newwin(curses.LINES-2,(curses.COLS//2)-2,1,1)
	lyricwindow.scrollok(1)
	creditwindow.scrollok(1)
	creditwindowbord.border()
	imagewindowbord.border()
	lyricwindowbord.border()
	creditwindowbord.refresh()
	imagewindowbord.refresh()
	lyricwindowbord.refresh()
	lyricsarray=[
	"Lyric test and such for a line.",
	"Another line.",
	"Yet another line arrives.",
	"\nTesting a line break.",
	"doing a thing",
	"blagh",
	"Yarr",
	"",
	"copy paste",
	"newpage",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste"
	]
	creditsarray=[
	"Test author: so and so",
	"Other author: blargh",
	"AUTHOR AUTHOR",
	"",
	"Oh wait another author",
	"need to test overflow",
	"doot",
	"come on",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste",
	"copy paste"
	]
	for totalline in range(0,len(lyricsarray)):
		if lyricsarray[totalline]=="newpage":
			lyricwindow.clear()
			lyricwindow.move(0,0)
			lyricwindow.refresh()
			for each in range(0,len(creditsarray[totalline])):
				if each<len(creditsarray[totalline]):
					creditwindow.addch(creditsarray[totalline][each])
					creditwindow.refresh()
				sleep(0.0666666)
		elif len(lyricsarray[totalline])>len(creditsarray[totalline]):
			for each in range(0,len(lyricsarray[totalline])):
				if each<len(lyricsarray[totalline]):
					lyricwindow.addch(lyricsarray[totalline][each])
					lyricwindow.refresh()
				if each<len(creditsarray[totalline]):
					creditwindow.addch(creditsarray[totalline][each])
					creditwindow.refresh()
				sleep(0.0666666)
		else:
			for each in range(0,len(creditsarray[totalline])):
				if each<len(lyricsarray[totalline]):
					lyricwindow.addch(lyricsarray[totalline][each])
					lyricwindow.refresh()
				if each<len(creditsarray[totalline]):
					creditwindow.addch(creditsarray[totalline][each])
					creditwindow.refresh()
				sleep(0.0666666)
	curses.nocbreak()
	curses.echo()
	curses.endwin()
