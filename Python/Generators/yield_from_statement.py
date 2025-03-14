from collections.abc import Sequence

# Without yield from
def subgenerator(n):
    for i in range(n):
        yield i

def main_generator_old(n):
    for val in subgenerator(n):
        yield val

# With yield from - more elegant
def main_generator_new(n):
    yield from subgenerator(n)
    
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, Sequence) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item