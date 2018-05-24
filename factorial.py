#4. Write a Python function to calculate the factorial of a number (a non-negativer integer). The fucntion accepts the number as an argument.

def factorial(n): 
	result = 1
	for i in range(2, n+1):
		result *= i
	return result

	
print ("Hello, let's play a cool game. Do you want to play? Write 'y' for yes or 'n' for no.")
y = input()
if y == "y":
	print("Great. I am a factorial magician. I can guess the factorial of ANY number. Here try it yourself. Write a number")
	x = int(esinput())
	print("Your number is " + str(x) + ". And its factorial is " + str(factorial(x)))
elif y == "n":
	print ("GTFO, then!")
else:
	print ("Couldn't understand you, dude. Try again.")



