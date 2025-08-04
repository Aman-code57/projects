# Calculate the factorial of a number

# Initialize variables
fact = 1
i = 1

# Get input from the user
num = int(input("Enter the number: "))

# Loop to calculate factorial
while i <= num:
    fact = fact * i
    i += 1

# Display the result
print("Factorial of", num, "is:", fact)
