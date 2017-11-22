from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
	ip=raw_input("IP Address: ")
	mc = Minecraft.create(ip, 4711)
	return mc

def head(mc,x,y,z):
	sphere(mc,x,y+5,z-10,5,246)
	eyes(mc,x,y,z)
	mc.setBlocks(x-1,y+11,z-9,x+1,y+11,z-11,57)
	mc.setBlock(x,y+12,z-10,247)
	
def eyes(mc,x,y,z):
	mc.setBlocks(x+1,y+6,z-5,x+3,y+6,z-6,0)
	mc.setBlocks(x-1,y+6,z-5,x-3,y+6,z-6,0)
	mc.setBlocks(x+1,y+5,z-6,x+3,y+6,z-6,0)
	mc.setBlocks(x-1,y+5,z-6,x-3,y+6,z-6,0)
	mc.setBlocks(x+1,y+6,z-7,x+3,y+6,z-7,10)
	mc.setBlocks(x-1,y+6,z-7,x-3,y+6,z-7,10)
	
def sphere(mc,x,y,z,radius,blockId):
	for x1 in range(radius*-1,radius+1):
		for y1 in range(radius*-1,radius+1):
			for z1 in range(radius*-1,radius+1):
				if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2:
					mc.setBlock(x+x1,y+y1,z+z1,blockId)
					
def main():
	mc=init()
	x,y,z=mc.player.getPos()
	y, z = (-43,z-9)
	head(mc,x,y,z)

main()
