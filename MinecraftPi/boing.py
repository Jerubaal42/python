from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep

def init():
	ip=raw_input("IP Address: ")
	mc = Minecraft.create(ip, 4711)
	return mc
	
def standOn(mc):
	x,y,z=mc.player.getTilePos()
	return mc.getBlock(x,y-1,z)
	
def main():
	mc=init()
	while True:
		if standOn(mc)==103:
			x,y,z=mc.player.getPos()
			mc.postToChat("Boing!")
			for each in range(1,16):
				sleep(0.001)
				mc.player.setPos(x,y+each,z)

main()
