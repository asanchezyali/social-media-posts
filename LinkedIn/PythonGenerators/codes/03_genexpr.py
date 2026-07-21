"""A generator expression (parentheses) is lazy; a list comprehension (brackets)
materialises everything. Same syntax, wildly different memory.
Run:  python 03_genexpr.py
"""
import sys

if __name__ == "__main__":
    as_list = [x * x for x in range(1_000_000)]
    as_gen = (x * x for x in range(1_000_000))

    print("list :", f"{sys.getsizeof(as_list):>10,} bytes")   # megabytes
    print("gen  :", f"{sys.getsizeof(as_gen):>10,} bytes")    # ~200 bytes

    # streamed sum — no list is ever built:
    print("sum  :", sum(x * x for x in range(1_000_000)))
