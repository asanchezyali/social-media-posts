def first_n_fibonacci(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Iterating with a for loop
fib = first_n_fibonacci(10)
for num in fib:
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34