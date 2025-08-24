"""
Program to Solve Algebraic Expressions of the form: ax² + bx + c

This script prompts the user to input the coefficients a, b, c of a quadratic expression,
and the value of x for which the expression is to be evaluated. It then calculates and
displays the result of the expression for the given value of x.
"""

# Print header
print("ALGEBRAIC EXPRESSION SOLVE")

# Input by user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Print Created expression 
print(f"The expression is {a}x² + {b}x + {c}")

# Input x value from user
x = int(input("Enter x: "))

# Calculate the expression 
result = a * x ** 2 + b * x + c

# Print the calculated result of algebraic expression
print(f"Result of {a}x² + {b}x + {c} when x={x} is:", result)
