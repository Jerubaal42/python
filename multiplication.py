def multi_table():
	while True:
		try:
			a=float(input('Number to multiply: '))
			break
		except:
			print("That's not a valid number...")
	for i in range(1,11):
		print('{0} x {1} = {2}'.format(a,i,a*i))
	exit
if __name__="__main__":
	multi_table()
