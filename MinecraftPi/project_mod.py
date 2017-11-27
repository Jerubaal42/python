#Damian's code modified to be relative instead of absolute - https://github.com/Damian42Blanco?tab=repositories
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
	ip=raw_input("IP Address: ")
	mc = Minecraft.create(ip, 4711)
	x, y, z = mc.player.getPos()
	return mc
	
def circle(mc,x,y,z):
	radius= 50
	for x1 in range(radius* -1,radius+1):
		for z1 in range(radius*-1, radius +1):
			if (x1**2)+(z1**2)<=(radius+1)**2:
				mc.setBlock(x+x1,-62,z+z1, 49)

def circle2(mc,x,y,z):
	radius= 50
	for x1 in range(radius* -1,radius+1):
		for z1 in range(radius*-1, radius +1):
			if (x1**2)+(z1**2)<=(radius+1)**2:
				mc.setBlocks(x+x1,-61,z+z1,x+x1,10,z+z1, 0)
				

def dome(mc,x,y,z):				
	radius= 50
	for x1 in range(radius* -1,radius+1):
		for y1 in range(radius*-1,radius+1):
			for z1 in range(radius*-1, radius +1):
				if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2 and (x1**2)+(y1**2)+(z1**2)>=(radius-1)**2 and y>=y:
					mc.setBlock(x+x1,y1-62,z+z1, 20)
				

	
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()  
	circle2(mc,x,y,z)
	mc.player.setPos(x,-50,z) 
	circle(mc,x,y,z)
	dome(mc,x,y,z)
	mc.postToChat("its working")


main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
