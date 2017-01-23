import random


def checkCowsAndBulls(numberToGuess: int, guessedNumber: int):
    strGuessedNumber = str(guessedNumber)
    strNumberToGuess = str(numberToGuess)

    cows = 0
    bulls = 0

    for k in range(0, 4):
        if strGuessedNumber[k] == strNumberToGuess[k]:
            cows += 1
        elif strGuessedNumber[k] in strNumberToGuess:
            bulls += 1

    return [cows, bulls]


if __name__ == "__main__":
    print("Welcome to the Cows and Bulls Game")
    numberToGuess = random.randint(1000, 9999)
    numberToGuess = 4018
    print("NumbertoGuess:", numberToGuess)

    while True:
        guessedNumber = input("Enter your guesses. To Exit, type 'q': ")
        if guessedNumber == 'q':
            break
        else:
            result = checkCowsAndBulls(numberToGuess, guessedNumber)
            print("Cows:", result[0], "Bulls:", result[1])
