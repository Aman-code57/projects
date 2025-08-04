# BMI Calculator

# Print header
print("      BMI CALCULATOR      ")

# Get input from user
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI result
print("Your BMI is:", round(bmi, 2))

# Determine BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
