def countdown(n):
    """A simple generator function that counts down from n to 1"""
    print("Starting countdown!")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

# Using the generator
counter = countdown(5)
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 5


