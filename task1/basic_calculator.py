# Basic calculator program

# Print header
print("THIS IS BASIC CALCULATOR")

# Input number by user
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))


# Giving choice and input from the user
choice = input("Choose Operation (+, -, /, *): ")


# Perform operation according user choice
if choice == "+":
    result = a + b
elif choice == "-":
    result = a - b
elif choice =="/":
    result = a / b 
elif choice =="*":
    result = a * b
else:
    # If user_choice is different from giving choice
     result = "Invalid operator"


# Print the result if the choice operation is executed 
print(f"THE {choice} RESULT OF NUMBER IS   :", result)
    