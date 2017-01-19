theNumber = int(input("Enter a number: "))

b = [x for x in range(1, theNumber + 1) if theNumber % x == 0]

print(b)
