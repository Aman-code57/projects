def my_function(*kids):
    """
    Prints the name of the youngest son from a list of children.

    Parameters:
    *kids (str): A variable number of children's names. Assumes the third child (index 2) is the youngest.

    Prints:
    The name of the youngest son.
    """
    print("The youngest son is " + kids[2])


my_function("arvind", "sanjay", "vineet")
