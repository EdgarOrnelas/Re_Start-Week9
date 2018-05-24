#13. Write a Python program to guess a number between 1 to 9

import random
n = random.randint(1, 10)
print ("Hello. This is a small guessing game")
print ("Please enter a number between 1 and 10")
a = int(input())
while a != n:
	print ("That is not the number, keep trying")
	a = int(input())
print("Great. Thanks for playing!")