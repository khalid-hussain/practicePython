def isPrime(n):
    counter = 2
    while counter != n:
        if n % counter == 0:
            return False
        counter += 1
    return True

    # divisors = [x for x in range(1, n + 1) if n % x == 0]
    # noOfDivisors = len(divisors)
    # if noOfDivisors > 2:
    #     return False
    # else:
    #     return True


print(isPrime(4))
print(isPrime(99))
print(isPrime(29))
print(isPrime(31))
