#finding the greatest number 

# Get input from user
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

# Compare numbers
if a > b and a > c :
    print("first number is the greatest")
elif b > a and b >c :
    print("second number is the greatest")
elif c > a and c > b :
    print("third number is greatest")
elif a == c and c > b :
    print("first and third number greatest and equal")
elif a == b and b > c :
    print("first number and second number is greatest and equal")
else:
    # Print if all number is same
    print("all are equal")