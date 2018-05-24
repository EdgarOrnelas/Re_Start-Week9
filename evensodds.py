#15. Write a Python program to count the number of even and odd numbers from a series of numbers.
print("Welcome to my program. It will take a list of numbers and tell you which of these are even and which are odds.")
howMany = int(input("How many numbers would you like to analyze? "))
numberList = []
print ("You will first create a list  of "+ str(howMany) + "numbers.")
for i in range (howMany):
	x = int(input("Please, type a number: "))
	howMany -= 1
	print ("You still have " + str(howMany) + " numbers to type") 
	numberList.append(x)

evens = []
odds = []
for n in numberList:
	if n%2 == 0:
		evens.append(n)
	else:
		odds.append(n)

iseven = len(evens)
isodd = len(odds)

print ("Your list was " + str(numberList))
print ("Total numbers: " + str(len(numberList)))
print ("These numbers are even : " + str(evens))
print ("These numbers are odds" + str(odds))
print ("Number of even numbers: " + str(iseven))
print ("Number of odd numbers: " + str(isodd))
