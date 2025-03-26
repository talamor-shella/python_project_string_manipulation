#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

#ask user input and use split method()
sentence = input("Enter a sentence: ").split()

#len() method to return the number of words
count = len(sentence)

#prints the number of words
print(f"The number of words is: {count}")