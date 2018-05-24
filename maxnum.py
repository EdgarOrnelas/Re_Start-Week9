#1 Write a Python fucntion to find the Max of  three numbers
def maxnumb(a, b, c):
	if a > b and a > c:
		print ("Your biggest number is " + str(a))
	elif a > b and a < c:
		print ("Your  biggest number is " + str(c))
	elif a < b and b > c:
		print ("Your biggest number is " + str(b))
	else:
		print ("You might have identical numbers. Please change this.")


maxnumb(9, 5, 4)
