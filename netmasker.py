#split binary into nibbles, not used
def nibblesplit(splitvar):
	endvar=''
	for each in range(0,len(splitvar)):
		if each%8==0 and each!=0:
			endvar=endvar+'.'
		elif each%4==0 and each!=0:
			endvar=endvar+' '
		endvar=endvar+splitvar[each]
	return(endvar)

#convert bin number to array
def conv_to_array(convvar):
	endvar=['','','','']
	arraynumb=0
	for each in range(0,len(convvar)):
		if each%8==0 and each!=0:
			arraynumb=arraynumb+1
		endvar[arraynumb]=endvar[arraynumb]+convvar[each]
	return(endvar)
	
#grabs the lowest bit of the netmask
def broadcaster(broadvar):
	testvar=0
	dabroadcast=0
	for each in range(0,len(broadvar)):
		if broadvar[each]==255:
			continue
		else:
			testvar=broadvar[each]
			break
	for each in range(0,8):
		if ((testvar<<each)&255)==128:
			dabroadcast=(((testvar<<each)&255)>>each)
			break
	if dabroadcast==0:
		dabroadcast=256
	return(dabroadcast)

#gets wildcard
def wildcard(wildinput):
	wildvar=[0,0,0,0]
	for each in range(0,len(wildinput)):
		wildvar[each]=((~(wildinput[each]))&255)
	return(wildvar)

#gets broadcast
def breadcaster(breadvar,broadvar):
	breadlord=['','','','']
	for each in range(0,len(breadvar)):
		breadlord[each]=((broadvar[each]+1)*((breadvar[each])//(broadvar[each]+1)))+broadvar[each]
	return(breadlord)

#gets possible subnets
def hostnumber(broadvar):
	testvar=0
	for each in range(0,9):
		if (broadvar<<each)==256:
			testvar=2**each
			break
	return(testvar)

#gets network id
def netidgen(ipadd,submask):
	netid=[-1,-1,-1,-1]
	for each in range(0,len(ipadd)):
		netid[each]=ipadd[each]&submask[each]
	return netid

#grabs min and max host addresses
def truehostnumber(bradvar,netvar):
	testvar=[0,0,0,0,0,0,0,0]
	for each in range(0,len(netvar)):
		if each==3:
			testvar[each]=netvar[each]+1
		else:
			testvar[each]=netvar[each]
	for each in range(0,len(bradvar)):
		if each==3:
			testvar[each+4]=bradvar[each]-1
		else:
			testvar[each+4]=bradvar[each]
	return(testvar)

#gets maximum hosts per network
def theotheronewasafake(wild):
	theonetruehost=0
	thetruewildcard=['','','','']
	theonetruewildcard='0b'
	theactualtruewildcard=0
	for each in range(0,len(wild)):
		thetruewildcard[each]=bin(wild[each])
	for each in range(0,len(thetruewildcard)):
		for eugh in range(2,len(thetruewildcard[each])):
			theonetruewildcard=theonetruewildcard+thetruewildcard[each][eugh]
	theactualtruewildcard=int(theonetruewildcard,2)
	theonetruehost=theactualtruewildcard-1
	return(theonetruehost)

if __name__=="__main__":
	fullip=['','','','','']
	shortip=[-1,-1,-1,-1]
	ipnumba=0
	masknumba=''
	fullmask=''
	damask=[-1,-1,-1,-1]
	damaskbin=["0b","0b","0b","0b"]
	netinput=input("Please input full ip address: (e.g., 192.168.1.8/24) \n	>>")
	for each in range(0,len(netinput)):
		if netinput[each]=="." or netinput[each]=="/":
			ipnumba=ipnumba+1
		else:
			fullip[ipnumba]=fullip[ipnumba]+netinput[each]
	for each in range(0,4):
		shortip[each]=int(fullip[each])
	for each in range(0,int(fullip[4])):
		masknumba=masknumba+'1'
	for each in range(0,32):
		try:
			fullmask=fullmask+masknumba[each]
		except:
			fullmask=fullmask+'0'
	damaskbinary=conv_to_array(fullmask)
	for each in range(0,len(damaskbinary)):
		damaskbin[each]=damaskbin[each]+damaskbinary[each]
	for each in range(0,len(damaskbin)):
		damask[each]=int(damaskbin[each],2)
	wildmask=wildcard(damask)
	breadlord=breadcaster(shortip,wildmask)
	subnets=hostnumber(broadcaster(damask))
	netid=netidgen(shortip,damask)
	hostses=truehostnumber(breadlord,netid)
	truehostses=theotheronewasafake(wildmask)
	print("Ip Address: {0}.{1}.{2}.{3}/{4}".format(fullip[0],fullip[1],fullip[2],fullip[3],fullip[4]))
	print("Subnet Mask: {0}.{1}.{2}.{3}".format(damask[0],damask[1],damask[2],damask[3]))
	print("Network Id: {0}.{1}.{2}.{3}".format(netid[0],netid[1],netid[2],netid[3]))
	print("Broadcast: {0}.{1}.{2}.{3}".format(breadlord[0],breadlord[1],breadlord[2],breadlord[3]))
	print("Minimum Host Ip: {0}.{1}.{2}.{3}".format(hostses[0],hostses[1],hostses[2],hostses[3]))
	print("Maximum Host Ip: {0}.{1}.{2}.{3}".format(hostses[4],hostses[5],hostses[6],hostses[7]))
	print("Maximum Hosts per Network: {0}".format(truehostses))
	print("Possible Subnets: {0}".format(subnets))
