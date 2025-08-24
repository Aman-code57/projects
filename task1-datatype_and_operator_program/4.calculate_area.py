"""
Program to Calculate the Area and Perimeter of a Circle

This script takes the radius of a circle from the user and calculates:
1. The area of the circle using the formula: π × r²
2. The perimeter (circumference) using the formula: 2 × π × r

It uses Python's built-in 'math' module for π (pi) value.
"""

# Import math module for pi constant
import math

# Print header
print("       FINDING AREA OF A CIRCLE       ")

# Get input from user
radius = float(input("Enter the radius of the circle (in cm): "))

# Calculate the area of the circle
area = math.pi * radius ** 2

# Print the area
print(f"The area of the circle is: {area:.2f} cm²")

# Print header
print("\n       FINDING PERIMETER OF THE CIRCLE       ")

# Calculate the perimeter of the circle
perimeter = 2 * math.pi * radius

# Print the perimeter
print(f"The perimeter (circumference) of the circle is: {perimeter:.2f} cm")
