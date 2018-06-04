from random import randint

def init():
	global itemlist,inventory,doorstatus
	itemlist={'key':'key'}
	inventory=[]
	doorstatus=[True]
	global playerposition
	playerposition="default"

def inputsplitter(inputstring):
	var0=''
	var1=''
	var2=''
	var3=''
	var4=''
	var5=''
	var6=""
	varnumber=0
	for each in inputstring:
		each=str(each.lower)
		if each == " ":
			varnumber=varnumber+1
		else:
			if varnumber==0:
				var0=str(var0)+str(each)
			elif varnumber==1:
				var1=str(var1)+str(each)
			elif varnumber==2:
				var2=str(var2)+str(each)
			elif varnumber==3:
				var3=str(var3)+str(each)
			elif varnumber==4:
				var4=str(var4)+str(each)
			elif varnumber==5:
				var5=str(var5)+str(each)
			elif varnumber==6:
				var6=str(var6)+str(each)
			else:
				continue
	vararray=[var0,var1,var2,var3,var4,var5,var6]
	return(vararray)
	
def defaultresponse(responsetype,randonumbo):
	if responsetype=='get':
		if randonumbo==0:
			return("That object is unobtainable.")
		elif randonumbo==1:
			return("I'm not sure you can grab that.")
		elif randonumbo==2:
			return("You try to grab that, and look rather silly whilst doing so.")
		else:
			return("You try to grab it for a while, then realize the futility of the effort.")
	elif responsetype=='cmd':
		if randonumbo==0:
			return("I don't understand.")
		elif randonumbo==1:
			return("I'm not sure I understand.")
		elif randonumbo==2:
			return("What?")
		else:
			return("I'm not sure how to do that.")
	elif responsetype=='use':
		if randonumbo==0:
			return("You fumble around a bit.")
		elif randonumbo==1:
			return("There's not much to use there.")
		elif randonumbo==2:
			return("I'm not sure you can use that.")
		else:
			return("I have no idea what you're trying to do.")
	elif responsetype=='look':
		if randonumbo==0:
			return("You look around.")
		elif randonumbo==1:
			return("You look at it.")
		else:
			return("You look at it for a while.")
	
def sampleroom():
	global itemlist,inventory,doorstatus
	while True:
		try:
			print("You are in a room.",end=" ")
			if 'key' in itemlist:
				print("There is a key on a table.")
			else:
				print()
			testinput=input()
			if testinput != '':
				textchoice=inputsplitter(testinput)
			print(textchoice)
			if textchoice[0]=="look":
				if textchoice[1]=="at":
					if textchoice[2]=="key":
						print("It is a key. It probably opens a lock.")
					elif textchoice[2]=="table":
						print("That is a table.",end=" ")
						if key in itemlist:
							print("There is a key on it.")
						else:
							print("As the key has been removed, it is no longer relevant to the story.")
					elif textchoice[2]=="door":
						print("It is a plain, wooden, unbreakable door.",end=" ")
						if doorstatus[0]==True:
							print("It is locked.")
						else:
							print()
					elif textchoice[2]=="room" or 'around':
						continue
					else:
						print(defaultresponse('look',randint(0,3)))
				else:
					if textchoice[1]=="key":
						print("It is a key. It probably opens a lock.")
					elif textchoice[1]=="table":
						print("That is a table.",end=" ")
						if key in itemlist:
							print("There is a key on it.")
						else:
							print("As the key has been removed, it is no longer relevant to the story.")
					elif textchoice[1]=="door":
						print("It is a plain, wooden, unbreakable door.",end=" ")
						if doorstatus[0]==True:
							print("It is locked.")
						else:
							print()
					elif textchoice[2]=="room" or 'around' or '':
						continue
					else:
						print(defaultresponse('look',randint(0,3)))
			if textchoice[0]=="get" or "grab" or "obtain":
				if textchoice[1]=='key':
					del itemlist['key']
					itemlist.append(key)
					print("You grab the key.")
				elif textchoice[1]=='table':
					print("You try to pick the table up, and discover it is bolted to the floor.")
				else:
					print(defaultresponse('get',randint(0,3)))
			if textchoice[0]=="pick" and textchoice[1]=="up":
				if textchoice[2]=='key':
					del itemlist['key']
					itemlist.append(key)
					print("You grab the key.")
				elif textchoice[2]=='table':
					print("You try to pick the table up, and discover it is bolted to the floor.")
				else:
					print(defaultresponse('get',randint(0,3)))
			if textchoice[0]=="leave" or "exit" or 'go':
				if doorstatus[0]==True:
					print("You are unable to leave, as the door (the only way out) is locked.")
				else:
					global playerposition
					playerposition='hallway'
					break
			if textchoice[0]=="use":
				if textchoice[1]=='key':
					doorstatus[0]=False
					inventory.remove('key')
					print('You use the key on the door. Both the key and the lock disappear.')
				elif textchoice[1]=='door':
					if doorstatus[0]==True:
						print("You are unable to leave, as the door (the only way out) is locked.")
					else:
						playerposition='hallway'
						break
				else:
					print(defaultresponse('use',randint(0,3)))
		except:
			print(defaultresponse('cmd',randint(0,3)))

if __name__ == '__main__':
	#init()
	print(inputsplitter(input()))

#while __name__ == '__main__':
#	global playerposition
#	if playerposition[0]=='d':
#		if playerposition=='default':
#			sampleroom()
#	elif playerposition[0]=='h':
#		if playerposition=='hallway':
#			exit()
	
