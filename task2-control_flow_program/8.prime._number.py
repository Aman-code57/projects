"""
Check Which Numbers in a List Are Prime

This program takes a list of integers input by the user,
checks each number, and prints those that are prime.
"""

# Input list by user, separated by spaces
list_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of integers
numbers = list(map(int, list_numbers.split()))

# Flag to check if any prime is found
found_prime = False

# Loop through each number to check if it's prime
for num in numbers:
    if num <= 1:
        continue  # Skip numbers less than or equal to 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break  # Not prime, exit inner loop
    else:
        # Number is prime
        print(f"{num} is a prime number")
        found_prime = True

if not found_prime:
    print("No prime numbers found in the list.")
