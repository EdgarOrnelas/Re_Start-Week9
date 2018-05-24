#8 Write a Python function that takes a list and returns a new list with unique elements for the first list

def unique(l):
	result = []
	for n in l:
		if n not in result:
			result.append(n)
	return result

giveMeUniques = [1, 1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9, 10, 10]
print(unique(giveMeUniques))
