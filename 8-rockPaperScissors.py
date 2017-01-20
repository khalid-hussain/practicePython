'''Improvements
1. Obscure player input
2. Sanitize user input
3. A GUI maybe?
'''

replay = "y"

while replay != "n":
    print("\nChoices")
    print("============")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors\n")

    play1 = int(input("Player One's move: "))
    play2 = int(input("Player Two's move: "))

    p1wins = "Player One WINS."
    p2wins = "Player Two WINS."
    noOnewins = "It's a draw."

    # Who wins
    if (play1 == 1):
        print(p2wins if play2 == 2 else p1wins)
    elif (play1 == 2):
        print(p2wins if play2 == 1 else p1wins)
    elif (play1 == 3):
        print(p2wins if play2 == 1 else p1wins)
    elif (play1 == play2):
        print(noOnewins)

    replay = input("Would you like to play again?: ")
