# List comprehension - loads all in memory
numbers_list = [x * 2 for x in range(1000000)]

# Generator expression - computes on-demand
numbers_gen = (x * 2 for x in range(1000000))

# Memory comparison
import sys
list_size = sys.getsizeof(numbers_list) 
# ~8.06 MB
gen_size = sys.getsizeof(numbers_gen)    
# ~200B