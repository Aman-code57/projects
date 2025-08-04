# Program to calculate the area of any shape
#math is predefine module for using math function and the value 
import math


# Print header
print("       FINDING AREA OF CIRCLE    ")

# Get input from user
radius = float(input("enter the radius of circle:  "))

# Calculate the area of cicle
area = math.pi * radius * radius # pi value is taken by math module

# Print the area 
print(f"THE AREA OF CIRCLE IS {area:.2f}cm²")

# Print header
print("       PERIMETER OF THE CICLE     ")

# Calculate the perimeter of circle
perimeter = 2 * math.pi * radius

# Print the perimeter
print(f"perimeter of circle is {perimeter:.2f}cm²")
