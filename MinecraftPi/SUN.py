from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
	ip=raw_input("IP Address: ")
	mc = Minecraft.create(ip, 4711)
	return mc
	
def sphere(mc,x,y,z,radius,blockId):
	for x1 in range(radius*-1,radius+1):
		for y1 in range(radius*-1,radius+1):
			for z1 in range(radius*-1,radius+1):
				if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2 and (x1**2)+(y1**2)+(z1**2)>=(radius-1)**2:
					mc.setBlock(x+x1,y+y1,z+z1,blockId)

def burn(mc,x,z,radius):
	for x1 in range(radius*-1,radius+1):
		for z1 in range(radius*-1,radius+1):
			if (x1**2)+(z1**2)<=(radius+1)**2:	
				y=mc.getHeight(x+x1,z+z1)
				mc.setBlock(x+x1,y,z+z1,10)

def main():
	mc=init()
	x, y, z = mc.player.getPos()
	burn(mc,x,z,10)
	sphere(mc,x,y+20,z,10,89)
	mc.postToChat("BEHOLD THE SUN!")

main()
