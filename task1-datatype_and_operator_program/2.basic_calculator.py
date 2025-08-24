"""
Basic Calculator Program

This program takes two numbers and a basic arithmetic operator (+, -, *, /) from the user,
performs the corresponding operation, and prints the result.
"""

# Print header
print("THIS IS A BASIC CALCULATOR")

# Input numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Input operation choice
choice = input("Choose Operation (+, -, *, /): ")

# Perform operation based on user choice
if choice == "+":
    result = a + b
elif choice == "-":
    result = a - b
elif choice == "*":
    result = a * b
elif choice == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
else:
    # If the operator is not valid
    result = "Invalid operator"

# Print the result
print(f"Result of {a} {choice} {b} is: {result}")
