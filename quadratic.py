def roots():
	while True:
		try:
			a=float(input('Enter A: '))
			b=float(input('Enter B: '))
			c=float(input('Enter C: '))
			break
		except:
			print("That's not a valid number...")
	D=(b*b-4*a*c)**0.5
	x_1=(-b+D)/(2*a)
	x_2=(-b-D)/(2*a)
	
	print('x1: {0}'.format(x_1))
	print('x2: {0}'.format(x_2))
if __name__ == '__main__':
    roots()
