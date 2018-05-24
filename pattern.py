#14. Write a Python program to construct the following pattern, using a nested for-loop

steps = int(input("Write the number of steps you want on your pattern: "))
for r in range(0, int(steps/2)):
	print("*" * r)
for r in range(int(steps/2), 0, -1):
	print("*" * r)


	
