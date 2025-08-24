"""
Check if a Number is Positive, Negative, or Zero,
and Determine if it is Even or Odd.
"""

# Input the number from the user
num = int(input("Enter the number to check: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
