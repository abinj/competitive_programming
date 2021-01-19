def iter_factorial(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    sum = n

    while n > 1:
        sum = sum * (n - 1)
        n -= 1
    return sum


print(iter_factorial(5))




def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n - 1)


print(factorial(5))