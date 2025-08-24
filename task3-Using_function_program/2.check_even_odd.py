def check_even_odd(number):
    """
    Determines whether a given number is even or odd and prints the result.

    Parameters:
    number (int): The integer to check.

    Prints:
    A message stating whether the number is even or odd.
    """
    if number % 2 == 0:  # Check if number is divisible by 2
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")


# Calling the function
check_even_odd(7)
