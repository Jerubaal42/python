from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep
from random import randint

def init():
	ip=raw_input("IP Address: ")
	mc = Minecraft.create(ip, 4711)
	return mc
	
def pew(mc,x,y,z):
	global live
	mc.setBlock(x-20,y+10,z,247)
	live=True
	while live==True:
		variablename=10
		randowidth=[]
		randoheight=[]
		for other in range(variablename):
			randowidth.append(randint(-10,10))
			randoheight.append(randint(0,10))
		for each in range(30):
			for other in range(variablename):
				mc.setBlock(x-10+each,y+randoheight[other],z+randowidth[other],46)
			testx,testy,testz=mc.player.getTilePos()
			if mc.getBlock(testx,testy,testz)==46 or mc.getBlock(testx,testy+1,testz)==46:
				mc.player.setPos(x,y,z)
			stayinalive(mc)
			sleep(0.5)
			for other in range(variablename):
				mc.setBlock(x-10+each,y+randoheight[other],z+randowidth[other],0)

def stayinalive(mc):
	global live
	blockEvent=mc.events.pollBlockHits()
	for each in blockEvent:
		x=each.pos.x
		y=each.pos.y
		z=each.pos.z
		if mc.getBlock(x,y,z)==247:
			live=False
			mc.postToChat("Augh! I will return foolish dude!")
			mc.setBlock(x,y,z,0)
			break

def main():
	mc=init()
	x,y,z=mc.player.getPos()
	pew(mc,x,y,z)

main()
