#10. Write a Python function that takesa number as a parameter and checks if the number is prime or not. Note: a prime number (or a prime) is a natural number greater than 1 that has no positive divisors  other than 1 and itself.
def is_prime(n):
	p = True
	for x in range(2, n):
		if n%x == 0:
			p = False
			break
		else:
			p = True

	if p == True:
		print ("Your number is a prime")
	else:
		print("Your  number is NOT a prime")


is_prime(21)