def find_fib_value(n):
    # The base cases
    if n <= 1:  # First number in the sequence
        return 0
    elif n == 2:  # Second number in the sequence
        return 1
    else:
        # Recursive call
        return find_fib_value(n - 1) + find_fib_value(n - 2)


print(find_fib_value(6))


nterms = int(input("How many terms?"))

n1, n2 = 0, 1
count =0

if nterms <=0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci Sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
