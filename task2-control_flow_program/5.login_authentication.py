"""
Simple Login System with Attempt Limit

This program prompts the user to enter a username and password,
checking the credentials against predefined values.
The user has a limited number of attempts before access is denied.
"""

# Constants
USERNAME = "amanraturi15"
PASSWORD = "aman897989"
PROFILE_NAME = "AMAN RATURI"
ATTEMPT_LIMIT = 3

# Initialize attempt count
attempt = 0

# Start login loop
while attempt < ATTEMPT_LIMIT:
    entered_username = input("Enter the username: ")
    entered_password = input("Enter the password: ")
    attempt += 1
    remaining_attempts = ATTEMPT_LIMIT - attempt

    if entered_username == USERNAME and entered_password == PASSWORD:
        print("LOGIN SUCCESSFUL!")
        print(f"Welcome, {PROFILE_NAME}!")
        break
    elif entered_username != USERNAME and entered_password != PASSWORD:
        if remaining_attempts > 0:
            print(f"Invalid username and password. You have {remaining_attempts} attempt(s) left.")
    else:
        if remaining_attempts > 0:
            print(f"Invalid password. You have {remaining_attempts} attempt(s) left.")

# If loop completed without successful login
if attempt == ATTEMPT_LIMIT and (entered_username != USERNAME or entered_password != PASSWORD):
    print("You have reached your attempt limit. Access denied.")
