def isPrime(n):
    divisors = [x for x in range(1, n + 1) if n % x == 0]
    noOfDivisors = len(divisors)
    if noOfDivisors > 2:
        return False
    else:
        return True


print(isPrime(4))
