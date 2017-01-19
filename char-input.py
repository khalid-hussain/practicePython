from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))

currentYear = date.today().year
yearYouWillbeHundred = currentYear + (100 - age)

print(yearYouWillbeHundred)

otherNumber = int(input("Input another number: "))

print(otherNumber * str(yearYouWillbeHundred))
