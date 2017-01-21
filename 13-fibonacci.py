def fibonacci(n: int = 1):
    if n == 1:
        return [1]
    else:
        result = [1, 1]
        while n - 2:
            result.append(result[-1] + result[-2])
            n -= 1
        return result


print(fibonacci(5))
# [1, 1, 2, 3, 5]
print(fibonacci(6))
# [1, 1, 2, 3, 5, 8]
print(fibonacci(7))
# [1, 1, 2, 3, 5, 8, 13]
