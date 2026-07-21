"""Don't write your own cache — the standard library ships one.

@cache (Python 3.9+) memoizes by arguments; it's the smaller, faster form of
lru_cache(maxsize=None). Use @lru_cache(maxsize=N) when you want a bounded cache.
Run:  python 05_lru_cache.py
"""
from functools import cache
from time import perf_counter


@cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start = perf_counter()
    print("fib(35) =", fib(35))
    print(f"took {(perf_counter() - start) * 1000:.2f} ms")
    print("cache:", fib.cache_info())   # hits, misses, maxsize, currsize
    fib.cache_clear()
