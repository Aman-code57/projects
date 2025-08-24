"""
Prompt the user to enter exactly 10 numbers separated by spaces,
then print only the even numbers from the input list.

If the user enters fewer or more than 10 numbers, an error message is shown.
"""

# Input list by user, separated by spaces
list_numbers = input("Enter 10 numbers separated by spaces: ")

# Split the input string into a list of integers
numbers = list(map(int, list_numbers.split()))

# Check if exactly 10 numbers were entered
if len(numbers) != 10:
    print("Please enter exactly 10 numbers.")
else:
    print("Even numbers in the list are:")
    for number in numbers:
        if number % 2 == 0:
            print(number)
