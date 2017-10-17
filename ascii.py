#save file as asc.py
def ascii():
	for i in range(256):
		c=chr(i)
		print(i,"-",c,"  ",end="")
		if (i%16==0):
			print("\n",end="")

def main():
	ascii()

main()
