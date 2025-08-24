def calculate():
    """
    Prompts the user to enter two numbers and an arithmetic operator,
    then performs the selected operation and prints the result.

    Supported operations:
        + : Addition
        - : Subtraction
        / : Division
        * : Multiplication

    If an invalid operator is entered, prints "Invalid operator".
    """
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    
    choice = input("Choose Operation (+, -, /, *): ")
    
    # Perform operation according to user choice
    if choice == "+":
        result = a + b
    elif choice == "-":
        result = a - b
    elif choice == "/":
        result = a / b 
    elif choice == "*":
        result = a * b
    else:
        # If user_choice is different from given choices
        result = "Invalid operator"
        
    print(f"{choice} result is {result}")


calculate()
