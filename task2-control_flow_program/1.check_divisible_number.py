"""
Program to Check Numbers from 1 to 100 Divisible by Both 3 and 5

This script loops through numbers from 1 to 100 and prints those
that are divisible by both 3 and 5 (i.e., divisible by 15).
"""

# Print header
print("Numbers between 1 and 100 divisible by both 3 and 5:")

# Loop through numbers from 1 to 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
