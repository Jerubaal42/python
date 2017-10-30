for x in range(40,48):
	for i in range(30,38):
		print ("\033[0;{0};{1}mCOLOR".format(i,x))
	for i in range(90,98):
		print ("\033[0;{0};{1}mCOLOR".format(i,x))
for x in range(100,108):
	for i in range(30,38):
		print ("\033[0;{0};{1}mCOLOR".format(i,x))
	for i in range(90,98):
		print ("\033[0;{0};{1}mCOLOR".format(i,x))
print("\033[0;97;40mDone")
