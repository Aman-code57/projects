"""
Assign a Letter Grade (A-F) Based on a Numeric Score

This program prompts the user to enter a score out of 100,
then assigns and prints a corresponding letter grade.
"""

# Input score from the user
score = int(input("Enter the score you obtained out of 100: "))

# Validate input
if score < 0 or score > 100:
    print("Invalid score. Please enter a value between 0 and 100.")
else:
    # Check score and assign grade
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    elif score >= 50:
        print("Grade: E")
    elif score >= 40:
        print("Grade: F")
    else:
        # Score below 40 is considered fail
        print("Fail")
