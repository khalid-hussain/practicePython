import random

totalGuesses = 0
correctGuesses = 0

while True:
    AIguess = random.randint(2, 6)
    userGuess = int(input("Enter your guess (1-9): "))
    totalGuesses += 1
    if (userGuess == AIguess):
        print("You guessed correctly.")
        correctGuesses += 1
    else:
        print("You guessed incorrectly.")
    if (input("Exit?: ") == "y"):
        print("Total Guesses:", totalGuesses)
        break
