# Conert days into weeks

# Get input from the user
days = int(input("Enter number of days: "))

# Calculate using floor division
weeks = days // 7

# Calculate the remaining days using Modulus 
remaining_days = days % 7

# Display result
print(f"{days} days = {weeks} week(s) and {remaining_days} day(s)")

    