from random import randint
import re

def shuffledeck():
	global deck
	deck=[]
	#Number value cards
	for value in range(2,11):
		tempvalue=S+str(value)
		deck.append(tempvalue)
		tempvalue=C+str(value)
		deck.append(tempvalue)
		tempvalue=H+str(value)
		deck.append(tempvalue)
		tempvalue=D+str(value)
		deck.append(tempvalue)
	#Spades face cards
	deck.append(SA)
	deck.append(SJ)
	deck.append(SQ)
	deck.append(SK)
	#Clubs face cards
	deck.append(CA)
	deck.append(CJ)
	deck.append(CQ)
	deck.append(CK)
	#Hearts face cards
	deck.append(HA)
	deck.append(HJ)
	deck.append(HQ)
	deck.append(HK)
	#Diamonds face cards
	deck.append(DA)
	deck.append(DJ)
	deck.append(DQ)
	deck.append(DK)

def handcheck(hand):
	global run
	pass

def carddraw():
	global deck
	card=deck.pop([randint(0,(len((deck)-1)))])
	return card

def handinit():
	hand=[]
	for each in range(5):
		hand.append(carddraw())
	return hand
	
def playgame(hand):
	global money
	global bet
	global run
	run=[]
	print("You have ${0}.".format(money))
	print("Your contains {0}{1}{2}{3}{4}.".format(hand[0],hand[1],hand[2],hand[3],hand[4]))
	while True:
		try:
			bet=input("Place your initial bet: ")
			if type(bet)!=int or bet>money:
				raise ValueError
			else:
				money=money-bet
				break
		except:
			print("Invalid value")
	cardrun(hand)
	cardrun(hand)
	cardrun(hand)
	handcheck(hand)
		
def cardrun(hand):
	global money
	global bet
	global run
	run.append(carddraw())
	while True:
		print("The run has ",end="")
		for each in run:
			print(each,end="")
		print("\n")
		print("You have ${0}.".format(money))
		print("Your current bet is ${0}.".format(bet))
		print("Your contains {0}{1}{2}{3}{4}.".format(hand[0],hand[1],hand[2],hand[3],hand[4]))
		while True:
			try:
				choice=input("You may \033[1;97;40mhold\033[0;97;40m or \033[1;97;40mraise.\033[0;97;40m")
				if choice=="hold" or choice=="raise":
					break
				else:
					raise ValueError
			except:
				print("Invalid Option")
		if choice=="hold":
			break
		elif choice=="raise":
			while True:
				try:
					betadd=input("Place your raise: ")
				if type(betadd)!=int or bet>money:
					raise ValueError
				else:
					money=money-betadd
					bet=bet+betadd
					break
				except:
					print("Invalid value")

if __name__=="__main__":
	global money
	money=1000

while __name__=="__main__":
	global deck
	global money
	deck=shuffledeck()
	hand=handinit()
