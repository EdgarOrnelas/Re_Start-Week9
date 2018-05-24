#20. Write a Python program to find numbers between 100 and 400 (both included) where each digit of the number is an even number. The numbers obtained should be in a comma-separated sequence.

allEvens=[]
for i in range(100, 401):
	n = str(i)
	if (int(n[0])%2==0) and (int(n[1])%2==0) and (int(n[2])%2==0):
		allEvens.append(n)

print(', ' .join(allEvens))