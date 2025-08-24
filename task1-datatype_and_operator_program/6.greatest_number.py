"""
Program to Find the Greatest of Three Numbers

This script takes three integer inputs from the user
and determines which number is the greatest.
It also handles cases where two or all three numbers are equal.
"""

# Get input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Compare numbers
if a > b and a > c:
    print("The first number is the greatest.")
elif b > a and b > c:
    print("The second number is the greatest.")
elif c > a and c > b:
    print("The third number is the greatest.")
elif a == b and b == c:
    print("All three numbers are equal.")
elif a == b and a > c:
    print("The first and second numbers are equal and greatest.")
elif a == c and a > b:
    print("The first and third numbers are equal and greatest.")
elif b == c and b > a:
    print("The second and third numbers are equal and greatest.")
else:
    # Handles edge cases like two numbers equal but not greatest
    print("There is no single greatest number.")
