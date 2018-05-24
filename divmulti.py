#12. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

divisors = []
multiples = []
for x in range (1499, 2701):
	if x%7==0:
		divisors.append(x)

for x in range(1499, 2701):
	if x%5 == 0:
		multiples.append(x)

allnumbers = divisors + multiples

def unique(l):
	result = []
	for n in l:
		if n not in result:
			result.append(n)
	return result


print(unique(allnumbers))