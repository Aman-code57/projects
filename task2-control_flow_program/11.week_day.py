"""
Program to Display the Weekday Based on a Given Number

Uses Python 3.10+'s match-case structure to print the name of the weekday
corresponding to the number entered by the user (1 = Monday, ..., 7 = Sunday).
"""

# Get input from user
day = int(input("Enter the day number (1–7): "))

# Match day number with weekday name
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number. Please enter a number between 1 and 7.")
