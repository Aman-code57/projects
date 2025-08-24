# Constants
DEFAULT_LAST_NAME = "Raturi"  # UPPER_CASE for constants

def print_full_name(first_name):
    """
    Print the full name by appending a default last name to the given first name.

    Parameters:
        first_name (str): The first name of the person.

    Returns:
        None
    """
    print(f"{first_name} {DEFAULT_LAST_NAME}")


# Calling the function
print_full_name("Aman")
