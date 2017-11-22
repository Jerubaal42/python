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
	global x2,y2,z2
	live=True
	while live==True:
		sleep(5)
		variablename=5
		variablename2=10
		randowidth=[]
		randoheight=[]
		randowidth2=[]
		randoheight2=[]
		mc.setBlocks(x-2,y,z-6,x+2,y+4,z-4,246)
		mc.setBlocks(x-2,y,z-7,x-2,y,z-4,0)
		mc.setBlocks(x+2,y,z-7,x+2,y,z-4,0)
		mc.setBlocks(x-2,y+4,z-4,x-2,y+4,z-4,0)
		mc.setBlocks(x+2,y+4,z-4,x+2,y+4,z-4,0)
		mc.setBlocks(x-1,y+1,z-6,x+1,y+3,z-4,0)
		for other in range(variablename):
			randowidth.append(randint(-1,1))
			randoheight.append(randint(1,3))
		for other in range(variablename2):
			randowidth2.append(randint(1,4))
			randoheight2.append(randint(1,4))
		for each in range(5):
			for other in range(variablename):
				mc.setBlock(x+randowidth[other],y+randoheight[other],z-5+each,46)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]+10,y+randoheight2[other]-13,z+3+each,46)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]-15,y+randoheight2[other]-13,z+3+each,46)
			testx,testy,testz=mc.player.getTilePos()
			if mc.getBlock(testx,testy,testz)==46 or mc.getBlock(testx,testy+1,testz)==46:
				mc.player.setPos(x,y,z)
			stayinalive(mc)
			sleep(0.5)
			for other in range(variablename):
				mc.setBlock(x+randowidth[other],y+randoheight[other],z-5+each,0)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]+10,y+randoheight2[other]-13,z+3+each,0)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]-15,y+randoheight2[other]-13,z+3+each,0)
		mc.setBlocks(x-2,y,z-6,x+2,y,z-4,0)
		mc.setBlocks(x-2,y+3,z-4,x+2,y+4,z-4,0)
		mc.setBlocks(x-2,y+1,z-5,x+2,y+2,z-4,0)
		mc.setBlocks(x-1,y+2,z-5,x+1,y+3,z-5,246)
		mc.setBlocks(x-1,y+1,z-6,x+1,y+3,z-6,246)
		for each in range(5,20):
			for other in range(variablename):
				mc.setBlock(x+randowidth[other],y+randoheight[other],z-5+each,46)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]+10,y+randoheight2[other]-13,z+3+each,46)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]-15,y+randoheight2[other]-13,z+3+each,46)
			testx,testy,testz=mc.player.getTilePos()
			if mc.getBlock(testx,testy,testz)==46 or mc.getBlock(testx,testy+1,testz)==46:
				mc.player.setPos(x,y-17,z+9)
			stayinalive(mc)
			sleep(0.5)
			for other in range(variablename):
				mc.setBlock(x+randowidth[other],y+randoheight[other],z-5+each,0)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]+10,y+randoheight2[other]-13,z+3+each,0)
			for other in range(variablename2):
				mc.setBlock(x+randowidth2[other]-15,y+randoheight2[other]-13,z+3+each,0)
	mc.postToChat("No! I have been defeated!")
	for stuff in range(3):
		sphere(mc,x,y+5,z-10,5,49)
		sphere(mc,x,y+5,z-10,5,246)
	sphere(mc,x,y+5,z-10,5,49)
	mc.setBlock(x2,y2,z2,247,2)
	

def sphere(mc,x,y,z,radius,blockId):
	for x1 in range(radius*-1,radius+1):
		for y1 in range(radius*-1,radius+1):
			for z1 in range(radius*-1,radius+1):
				if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2:
					mc.setBlock(x+x1,y+y1,z+z1,blockId)

def stayinalive(mc):
	global live
	global x2,y2,z2
	blockEvent=mc.events.pollBlockHits()
	for each in blockEvent:
		x=each.pos.x
		y=each.pos.y
		z=each.pos.z
		if mc.getBlock(x,y,z)==247:
			live=False
			mc.setBlock(x,y,z,247,1)
			x2=x
			y2=y
			z2=z
			break

def main():
	mc=init()
	x,y,z=mc.player.getPos()
	y,z=(-43,z-9)
	pew(mc,x,y,z)

main()
