# Program to reverse the user given word

# Input by user given
word = input("enter the word you want to reverse: ")

# Intialize the reversed string is empty
reversed_word = ""

# For loop for string reverse 
for char in word:
    reversed_word = char + reversed_word     # apppend word

# Print the reversed word
print("Reversed:", reversed_word)
