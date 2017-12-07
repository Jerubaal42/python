#Dicegame 2.0
import random
def diceroll():
	random.seed()
	d1=random.randint(1,6)
	d2=random.randint(1,6)
	sum=(d1+d2)
	temp_list=[]
	for active_bet, bet_data in bet_dict.items():
		if sum in bet_data[1]:
			print("You WON and received",bet_data[0],"moneys.")
			global cash
			cash=cash+(bet_data[0]*2)
			temp_list.append(active_bet)
		elif sum in bet_data[2]:
			print("You LOST and lost",bet_data[0],"moneys.")
			temp_list.append(active_bet)
		elif 7 in bet_data[1] or 11 in bet_data[1]:
			print("Your initial POINT was missed and is now",sum,".")
			bet_data[1]=[sum]
			bet_data[2]=[7]
		else:
			print("Your bet of",bet_data[0],"is still running.")
	print(bet_dict)
	print(temp_list)
	for i in temp_list:
		if i in bet_dict:
			del bet_dict[i]
def bet(money):
	for i in range(26):
		if i in bet_dict:
			continue
		else:
			bet_dict[i]=[money,[7,11],[2,3,12]]
			global cash
			cash=cash-money
			break
	diceroll()

if __name__=="__main__":
	global cash
	global bet_dict
	bet_dict={}
	cash=1000
	while True:
		print("You have",cash,"cash.")
		choice=input('You may \'bet\' more money, \'roll\' the dice, or \'exit\' the game: ')
		if choice=='bet':
			betamount=int(input('Insert bet amount: '))
			if betamount>cash or betamount<=0:
				continue
			bet(betamount)
		if choice=='roll':
			diceroll()
		if choice=='exit':
			exit()
