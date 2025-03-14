# List comprehension (creates entire list in memory)
squares_list = [x*x for x in range(1000000)]  # Uses more memory

# Generator expression (creates generator object)
squares_gen = (x*x for x in range(1000000))   # Uses minimal memory

# Using the generator expression
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4