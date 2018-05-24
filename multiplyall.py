#7. Write a Python function to multiply all the numbers in a list

def multiall(l):
	result = 1
	for n in l:
		result *= n
	return result

multiplyTheseNumbers = [2, 4, 6, 8]
print(multiall(multiplyTheseNumbers))