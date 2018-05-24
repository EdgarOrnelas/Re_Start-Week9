#5. Write a Python fucntion to print even numbers from a given list

def evens(l):
	evenumbers = []
	for i in l:
		if i%2==0:
			evenumbers.append(i)
	return evenumbers
		
areTheseEvens = [5, 8, 9, 12, 24, 52, 84, 124, 129, 251]

print ("These a are your even numbers: ")
print (evens(areTheseEvens))
