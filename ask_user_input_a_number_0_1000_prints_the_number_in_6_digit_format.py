#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

#ask user input
number = input("Enter a number: ")

#use zfill method
six_digit = number.zfill(6)

#print the user input 
print(six_digit)