import tracemalloc

# Start memory monitoring
tracemalloc.start()

# Create a large list
large_list = [i * i for i in range(1000000)]
list_snapshot = tracemalloc.take_snapshot()
list_size = sum(stat.size for stat in list_snapshot.statistics('filename'))

# Reset monitoring
tracemalloc.stop()
tracemalloc.start()

# Create an equivalent generator
large_gen = (i * i for i in range(1000000))
gen_snapshot = tracemalloc.take_snapshot()
gen_size = sum(stat.size for stat in gen_snapshot.statistics('filename'))

# Compare memory usage
print(f"List memory: {list_size / 1024 / 1024:.2f} MB")
print(f"Generator memory: {gen_size / 1024 / 1024:.2f} MB")
print(f"Memory ratio: {list_size / gen_size:.0f}x")

# Create a large list
large_list = [i * i for i in range(1000000)]
list_snapshot = tracemalloc.take_snapshot()
list_size = sum(stat.size for stat in list_snapshot.statistics('filename'))

# Reset monitoring
tracemalloc.stop()
tracemalloc.start()

# Create an equivalent generator
large_gen = (i * i for i in range(1000000))
gen_snapshot = tracemalloc.take_snapshot()
gen_size = sum(stat.size for stat in gen_snapshot.statistics('filename'))

# Compare memory usage
print(f"List memory: {list_size / 1024 / 1024:.2f} MB")
print(f"Generator memory: {gen_size / 1024 / 1024:.2f} MB")
print(f"Memory ratio: {list_size / gen_size:.0f}x")