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
		
def convertkmmi():
	def print_menu():
		print('1. Kilometers to Miles')
		print('2. Miles to Kilometers')
	
	def km_miles():
		while True:
			try:
				km=float(input('Enter distance in kilometers: '))
				break
			except:
				print("That's not a valid number...")
		miles=km/1.609
		print('Distance in miles: {0}'.format(miles))
	
	def miles_km():
		while True:
			try:
				miles=float(input('Enter distance in miles: '))
				break
			except:
				print("That's not a valid number...")
		km=miles*1.609
		print('Distance in kilometers: {0}'.format(km))
	
	print_menu()
	while True:
		try:
			choice=input('Which conversion would you like to do?: ')
			if choice=='1':
				km_miles()
				break
			if choice=='2':
				miles_km()
				break
			else:
				raise ValueError
		except:
			print('Invalid Decision')
	exit
	
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
	
if __name__=='__main__':
	print("Mathemagic v1.0")
	print("1. Factorization")
	print("2. Multiplication Table")
	print("3. Mile-Kilometer Conversion")
	print("4. Quadratic Roots")
	while True:
		try:
			choice=int(input('What would you like to calculate?: '))
			if choice==1:
				factors()
				break
			if choice==2:
				multi_table()
				break
			if choice==3:
				convertkmmi()
				break
			if choice==4:
				roots()
				break
			else:
				raise ValueError
		except:
			print('Invalid Choice')
