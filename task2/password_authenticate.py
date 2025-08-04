#Repeatedly asks for a password until the correct one is entered

#Constant
USERNAME = "amanraturi"
USER_PASSWORD = "505757"

# Input password from user
password = input("enter the password: ")

# Start loop for checking password
while password != USER_PASSWORD:
    print("invalid password")     
    password = input("enter the password: ")

# Print the username and password if password is matched
print(f"password is correct:{USER_PASSWORD}")
print(f"Your welcome {USERNAME}") 