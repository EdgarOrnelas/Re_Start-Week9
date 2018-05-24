#3. Write a Python function to create and print a list where the values are square of numbers betwwen 1 and 30.
def squarenum(n):
	square = 0
	if n**2 <= 30:
		square = n**2
		print ("Your number is " + str(n) + ". And the square of this number is " + str(square))
	else:
		print("The square of the number you input is over 30!!!")

squarenum(5)