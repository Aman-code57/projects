"""
Program to Convert Days into Weeks and Days

This script takes the number of days as input from the user,
then converts and displays the equivalent number of full weeks
and remaining days.
"""

# Get input from the user
days = int(input("Enter the number of days: "))

# Calculate full weeks using floor division
weeks = days // 7

# Calculate remaining days using modulus operator
remaining_days = days % 7

# Display the result
print(f"{days} day(s) = {weeks} week(s) and {remaining_days} day(s)")
