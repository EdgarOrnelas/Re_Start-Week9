#6. Write a Python function to summ all the numbers in a list

def sumall(l):
	result = 0
	for n in l:
		result += n
	return result

sumTheseNumbers = [25, 25, 25, 25, 50]

print (sumall(sumTheseNumbers))
