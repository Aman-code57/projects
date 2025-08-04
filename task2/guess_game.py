#constants
TARGET_NUMBER = 25
MAXIMUM_GUESS = 3

#intialize the guess
guess_count = 0

#start the gusessing loop
while guess_count < MAXIMUM_GUESS:
    num = int(input("enter the guess number: "))
    guess_count += 1
    
    if(num == target_number):
        print("your guess is right")
        break
    elif num<20:
        print("number is too less")
    elif num>30:
        print("number is too high")
    else:
        print("invalid guess.you are close")

#If loop completed without right guess        
if num != TARGET_NUMBER:
    print(f"you reach out guesses.the target number is {TARGET_NUMBER}")
