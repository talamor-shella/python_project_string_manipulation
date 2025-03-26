#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#ask user input with title() method
fullname = input("Enter your fullname: ").title()

#use replace method to remove the spaces
pascal_case = fullname.replace(" ","")

#prints the input in pascal case
print(f"Your fullname is(in pascal case): {pascal_case}")