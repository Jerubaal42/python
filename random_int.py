from random import randint
def ranint():
	r=randint(65,91)
	return r
def main():
	for r in range(10):
		rint=ranint()
		print(rint,end="")
main()
