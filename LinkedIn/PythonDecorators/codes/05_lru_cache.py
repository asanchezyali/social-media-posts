"""Don't write your own cache — the standard library ships one.

lru_cache memoizes by arguments, turning exponential fib into linear.
Run:  python 05_lru_cache.py
"""
from functools import lru_cache
from time import perf_counter


@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start = perf_counter()
    print("fib(35) =", fib(35))
    print(f"took {(perf_counter() - start) * 1000:.2f} ms")
    print("cache:", fib.cache_info())   # hits, misses, maxsize, currsize
    fib.cache_clear()
