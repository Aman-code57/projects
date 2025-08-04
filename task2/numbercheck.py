# Input the number given by user
num = int(input("Enter the number to check: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("Number is a positive number")
elif num < 0:
    print("Number is a negative number")
else:
    print("Number is zero")

# Check if the given number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
