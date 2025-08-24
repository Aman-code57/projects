"""
Unit Conversion: Inches to Centimeters

This program takes a length in inches as input from the user
and converts it to centimeters using the formula:
1 inch = 2.54 centimeters.
"""

# Print header
print("     UNIT CONVERSION: INCHES TO CENTIMETERS     ")

# Get input from the user
inch = float(input("Enter the length in inches to convert: "))

# Calculate the result
result = inch * 2.54

# Display the result
print(f"{inch} inch(es) = {result:.2f} centimeter(s)")
