# Intialize the fact and loop start value
fact = 1
i= 1

# Get input from user
num = int(input("enter the number: "))


# start loop
while i <= num:
    fact = fact * i
    i += 1
    print(fact)
