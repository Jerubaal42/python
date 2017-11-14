import mcpi.minecraft as minecraft

def init():
	ip=raw_input("IP Address: ")
	mc=minecraft.Minecraft.create(ip,4711)
	return mc

def main():
	mc=init()
	for y in range(64,-1,-1):
		mc.setBlocks(-128,y,-128,128,y,128,0)
	mc.setBlocks(-128,-1,-128,128,-1,128,2)
	for y in range(-2,-5,-1):
		mc.setBlocks(-128,y,-128,128,y,128,3)
	for y in range(-5,-64,-1):
		mc.setBlocks(-128,y,-128,128,y,128,1)
	mc.setBlocks(-128,-64,-128,128,-64,128,7)
	mc.postToChat("The world has been FLATTENED.")

main()
