"""
Number Guessing Game

The user has a limited number of attempts to guess the target number.
The program provides feedback if the guess is too low, too high,
or close to the target number.
"""

# Constants
TARGET_NUMBER = 25
MAXIMUM_GUESS = 3

# Initialize the guess count
guess_count = 0

# Start the guessing loop
while guess_count < MAXIMUM_GUESS:
    num = int(input("Enter your guess: "))
    guess_count += 1
    
    if num == TARGET_NUMBER:
        print("Your guess is right!")
        break
    elif num < 20:
        print("Number is too low.")
    elif num > 30:
        print("Number is too high.")
    else:
        print("Invalid guess. You are close!")

#
