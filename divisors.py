#9. Write a Python functino that takes a natural number greater than 1 and returns the number of its positivedivisors, except 1 and the number itself

def divisors(l):
	result = []
	for  n in range(1, l):
		if l%n == 0:
			result.append(n)
	return result

giveMeDivisor = 85
print(divisors(giveMeDivisor))