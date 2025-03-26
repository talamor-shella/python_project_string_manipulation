#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

#ask user input with lstrip() method
fullname = input("Enter your fullname: ").lstrip()

#print the user input 
print(f"Your fullname is: {fullname}")