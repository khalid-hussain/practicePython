theNumber = int(input("Enter a number: "))

num = int(input("Enter <num>: "))
check = int(input("Enter <check>: "))

if theNumber % 2 == 0:
    if theNumber % 4 == 0:
        print("The number is a multiple of four, thus even.")
    else:
        print("The number is even.")
else:
    print("The number is odd.")

if num % check == 0:
    print("<check> divides evenly into <num>")
else:
    print("<check> doesn't divide evenly into <num>")
