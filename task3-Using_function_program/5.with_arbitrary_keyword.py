def my_function(**kid):
    """
    Prints the last name of a person from given keyword arguments.

    Parameters:
    **kid: Arbitrary keyword arguments representing details about a person.
           Expects a key 'lname' for the last name.

    Prints:
    The last name associated with the key 'lname'.
    """
    print("His last name is " + kid["lname"])


my_function(fname="aman", lname="raturi")
