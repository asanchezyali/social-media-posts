"""A practical decorator: time how long a function takes.

Run:  python 04_timer.py
"""
from functools import wraps
from time import perf_counter


def timer(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        start = perf_counter()
        try:
            return fn(*a, **k)
        finally:
            elapsed = perf_counter() - start
            print(f"{fn.__name__} took {elapsed * 1000:.2f} ms")
    return wrapper


@timer
def slow_sum(n):
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    print("sum:", slow_sum(1_000_000))
