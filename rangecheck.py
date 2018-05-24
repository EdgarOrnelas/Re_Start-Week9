#Write a Python function to check wether a number is in a given range.
def rangecheck(i):
	if i >= 0 and i <= 10:
		print("You number is between 0 and 10")
	elif i > 10 and i <= 100:
		print("Your number is betwwen 11 and 100")
	elif i > 101 and i <= 500:
		print("Your number is between 101 and 500")
	else:
		print("Sorry. I only know how to count until 500. Come back later when I learn more numbers")

rangecheck(5)
rangecheck(15)
rangecheck(250)
rangecheck(852)