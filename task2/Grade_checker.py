# Assigns a letter grade (A–F) based on a numeric score

# Input score from the user
score = int(input("Enter the score you obtained out of 100: "))

# Check score and assign grade
if score >= 90:
    print("GRADE A")
elif score >= 80:
    print("GRADE B")
elif score >= 70:
    print("GRADE C")
elif score >= 60:
    print("GRADE D")
elif score >= 50:
    print("GRADE E")
elif score >= 40:
    print("GRADE F")
else:
    # If all conditions fail, print FAIL
    print("FAIL")
