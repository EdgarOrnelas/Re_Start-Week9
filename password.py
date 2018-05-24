#19. Write a Python program to check the validity of a password input by users

import re
print ("Hello, I will guide you to create a secure password for this site.")
print ("Your password can be anything you like, but it has to include the following elements:")
print ("It has to be between 6 and 16 characters")
print ("At least ONE lower-cap ('a' to 'z') and ONE Cap letter ('A' to 'Z')")
print ('At least ONE number')
print ("Aaaand... at least ONE of these special characters: '$', '#', '@'")
print ("That is it! I hope you have a good password in mind. Please input your password below:")
p = input(' ')
incorrectPassword = True
while incorrectPassword:
	if len(p) < 6:
		print ("Your password is too short")
		p = input("Try again: ")
		break
	elif len(p) > 16:
		print ("Your password is too long")
		p = input("Try again: ")
		break
	elif not re.search('[a-z]', p):
		print ("You missed a lower-cap letter")
		p = input("Try again: ")
		break
	elif not re.search('[A-Z]', p):
		print ("You missed a CAPS letter")
		p = input("Try again: ")
		break
	elif not re.search('[0-9]', p):
		print ("You missed a number")
		p = input("Try again: ")
		break
	elif not re.search ('[$#@]', p):
		print ("You missed one of the special characters")
		p = input("Try again: ")
		break
	else:
		print ("Great! Your password has been stored")
		incorrectPassword = False
		break

if incorrectPassword:
	print ("The password you entered is not valid")



