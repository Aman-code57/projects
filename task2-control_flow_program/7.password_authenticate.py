"""
Repeatedly asks for a password until the correct one is entered.
"""

# Constants
USERNAME = "amanraturi"
USER_PASSWORD = "505757"

# Input password from user
password = input("Enter the password: ")

# Start loop for checking password
while password != USER_PASSWORD:
    print("Invalid password. Please try again.")     
    password = input("Enter the password: ")

# Print welcome message if password is correct
print(f"Password is correct: {USER_PASSWORD}")
print(f"Welcome, {USERNAME}!")
