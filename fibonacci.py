#16. Write a Python function to get the Fibonacci series between 0 to 50

a = 1
b = 0
print (b)
while a < 50:
	c = b #0 1 1 2 3 5 8 13 21 
	b = a #1 1 2 3 5 8 13 21 34
	a = c + b #1 2 3 5 8 13 21 34 55
	print (a - c)

