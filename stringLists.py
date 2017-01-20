# theWord = input("Enter a word: ")
theWord = "race car"

# Remove spaces
theWord = theWord.replace(" ", "")

# Check the word with its mirrored version
if theWord == theWord[::-1]:
    print("You've entered a palindrome.")
else:
    print("You didn't enter a palindrome.")
