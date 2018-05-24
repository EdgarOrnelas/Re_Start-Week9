#18. Write a Python program which takes two digits: m (row) and n (column) as input an generates a two dimensional array. The element value in the i-th row and the j-th column of the array should be i*j

r = int(input("Input the number of rows: "))
c = int(input("Input the number of columns: "))
multiList = [[0 for col in range(c)] for row in range(r)]

for row in range(r):
	for col in range(c):
		multiList[row][col]=row*col

print (multiList)