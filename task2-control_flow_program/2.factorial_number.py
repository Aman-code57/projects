"""
Program to Calculate the Factorial of a Number Using a While Loop

This script prompts the user to enter a non-negative integer and
calculates its factorial by multiplying numbers from 1 to the given number.
"""

# Initialize factorial and loop start value
fact = 1
i = 1

# Get input from user
num = int(input("Enter a non-negative number: "))

# Validate input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Start loop
    while i <= num:
        fact = fact * i
        i += 1
    
    # Display final result
    print(f"The factorial of {num} is: {fact}")
