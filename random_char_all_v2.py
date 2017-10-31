from random import randint
def ascii_table():
	asciitable=[]
	for i in range(33,127):
		asciitable.append(chr(i))
	return asciitable
def main():
	asciitable=ascii_table()
	asciitablelist=[]
	x=len(asciitable)-1
	while len(asciitablelist)!=len(asciitable):
		r=randint(0,x)
		print(asciitable[r],end=" ")
		if asciitable[r] not in asciitablelist:
			asciitablelist.append(asciitable[r])
main()
print()
