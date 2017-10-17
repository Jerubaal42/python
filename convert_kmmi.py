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
if __name__ == '__main__':
    convertkmmi()
