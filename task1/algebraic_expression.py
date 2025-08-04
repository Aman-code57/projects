# Program to Solve algebraic expressions

# Print header
print("ALGEBRAIC EXPRESSION SOLVE")

# Input by user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Print Created expression 
print(f"the expression is {a}x² + {b}x + {c}")

# Input x value from user
x = int(input("Enter x: "))

# Calculate the expression 
result = a * x ** 2 + b * x + c

# Print the calculated result of algebraic expression
print(f"Result of {a}x² + {b}x + {c} when x={x} is:", result)
