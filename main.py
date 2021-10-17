# Brian D. Christman
# Purpose: to generate a random integer between 1 and 100 and allow a user to try and
# guess the number. The number of guesses are counted and printed once the game is complete.

# Import the packages used in this program
import random

# Generate and print a random integer between 1 and 100
correctNumber = random.randint(1, 100)
# print(correctNumber)  # Uncomment to validate that the program is working properly

# Print the introduction and rules to the number guessing game
print("Welcome to the number guessing game!")
print("To play, enter an integer between 1 and 100 (no decimals) in the guess prompt.")
print("To stop, enter 'stop' in the guess prompt.")
print()

# Create the guess counter, stop options, and try block and ask for the first guess from the user
try:
    guessCtr = 0
    stop = ['stop', 'Stop', 'STOP']
    number = input("Please enter your number guess (an integer between 1 and 100): ")

    # Assess the user's input and print out whether the guess was valid and increment the counter
    # or have the user guess again or stop. Stop the game and print the number of guesses made
    # if the user guesses correctly.
    while True:
        if number in stop:
            break
        elif not number.isnumeric():
            print("You have not entered an integer between 1 and 100. This guess did not count.\n")
            number = input("Please enter your number guess (an integer between 1 and 100): ")
        elif int(number) not in range(1, 101):
            print("You have not entered an integer between 1 and 100. This guess did not count.\n")
            number = input("Please enter your number guess (an integer between 1 and 100): ")
        elif int(number) < correctNumber:
            print("Your guess is too low.\n")
            guessCtr = guessCtr + 1
            number = input("Please enter your number guess (an integer between 1 and 100): ")
        elif int(number) > correctNumber:
            print("Your guess is too high.\n")
            guessCtr = guessCtr + 1
            number = input("Please enter your number guess (an integer between 1 and 100): ")
        else:
            print("Your guess is correct! Congratulations!")
            guessCtr = guessCtr + 1
            print(f"It took you {guessCtr} guesses to pick the correct number!\n")
            break

# Check for errors and print if an error occurred
except Exception as e:
    print("An error has occurred.")
    print(e)

# Print a thank you message and close the game out
print("Thank you for playing the number guessing game!")
