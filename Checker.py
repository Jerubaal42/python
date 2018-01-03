def listMaker(checker):
	x=0
	checked=[]
	while x<100:
		checked.append(x)
		x=x+checker
	return checked

def checkForDups(dup1,dup2):
	checked=[]
	for each in dup2:
		if each in dup1:
			checked.append(each)
	return checked
	
numba2=listMaker(2)
numba3=listMaker(3)
numba5=listMaker(5)
numba7=listMaker(7)
"""numba11=listMaker(11)
numba13=listMaker(13)
numba17=listMaker(17)
numba19=listMaker(19)"""

Test1=checkForDups(numba2,numba3)
Test2=checkForDups(numba5,numba7)
"""Test3=checkForDups(numba11,numba13)
Test4=checkForDups(numba17,numba19)"""
Test5=checkForDups(Test1,Test2)
#Test6=checkForDups(Test3,Test4)
#Test7=checkForDups(Test5,Test6)

print(numba2)
print(numba3)
print(numba5)
print(numba7)
print(Test5)
