# Week days check

# Get input from user
day = int(input("enter the day number: "))

# Create option using match case
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
