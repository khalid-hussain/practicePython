import math


# def isPrimeOld(n: int):
#     counter = 2
#     while counter != n:
#         if n % counter == 0:
#             return False
#         counter += 1
#     return True


def isPrime(n: int):
    counter = 2
    root = round((math.sqrt(n)))
    while counter != root + 1:
        if n % counter == 0:
            return False
        counter += 1
    return True


print(isPrime(4))
print(isPrime(99))
print(isPrime(29))
print(isPrime(31))
