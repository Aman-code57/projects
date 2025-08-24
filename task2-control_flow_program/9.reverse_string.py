"""
Program to Reverse a Word Given by the User

This script takes a word as input and reverses it using a loop.
"""

# Input word from the user
word = input("Enter the word you want to reverse: ")

# Initialize the reversed string as empty
reversed_word = ""

# Loop through the characters to reverse the word
for char in word:
    reversed_word = char + reversed_word  # Prepend character

# Print the reversed word
print("Reversed:", reversed_word)
