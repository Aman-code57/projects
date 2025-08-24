"""
BMI (Body Mass Index) Calculator

This program calculates the Body Mass Index based on user input of weight (in kilograms)
and height (in meters). It then categorizes the BMI result as Underweight, Normal,
Overweight, or Obese.
"""

# Print header
print("      BMI CALCULATOR      ")

# Get input from user
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI result rounded to 2 decimal places
print("Your BMI is:", round(bmi, 2))

# Determine and display BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
