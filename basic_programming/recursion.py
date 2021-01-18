def factorial(x):
    if x is 0:
        return 1
    return x*factorial(x-1)


factorial(5)
