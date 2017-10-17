from random import randint
def ascii_table():
	global asciitable
	asciitable=[]
	for i in range(33,127):
		asciitable.append(chr(i))
def main():
	ascii_table()
	x=len(asciitable)-1
	while len(asciitable)!=0:
		r=randint(0,x)
		print(asciitable[r],end=" ")
		del asciitable[r]
		x=x-1
main()
