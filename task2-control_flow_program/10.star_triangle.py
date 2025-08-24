"""
Pattern Generator: Centered Triangle of Asterisks

This program prompts the user to enter the number of rows,
then prints a pyramid-shaped pattern using asterisks (*).
"""

# Input number of rows from the user
rows = int(input("Enter the number of rows: "))

# Loop to generate each row
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(1, rows - i + 1):
        print(" ", end="")

    # Print stars (2*i - 1 for pyramid shape)
    for k in range(1, 2 * i):
        print("*", end="")

    # Move to the next line after each row
    print()
