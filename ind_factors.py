def factors():
	while True:
		try:
			a=int(input('Number to factor: '))
			if a<=0:
				raise ValueError
			else:
				break
		except:
			print("That's not a valid number...")
	print('The factors of ',a,' are:')
	for i in range(1,a+1):
		if a%i==0:
			print(i)
	exit
if __name__=='__main__':
	factors()
