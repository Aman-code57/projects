# Check in the list to check which numbers are prime

# Input list by user, separated by spaces
list_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of integers
numbers = list(map(int, list_numbers.split()))

# Loop through each number to check if it's a prime number
for num in numbers:
    if num <= 1:
        continue  # Skip numbers less than or equal to 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break  # Exit loop if number is divisible (not prime)
    else:
        # Print the number if it is prime
        print(f"{num} is a prime number")
 

