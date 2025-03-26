#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#ask user input fullname and use lower method
fullname = input("Enter your fullname: ").lower()

#use replace method 
snake_case = fullname.replace(" ","_")

#print the input in snake case