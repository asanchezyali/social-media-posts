"""A function with `yield` returns a generator: a lazy iterator that produces
values one at a time, on demand. Calling it runs no code yet.
Run:  python 01_basic.py
"""


def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1


if __name__ == "__main__":
    g = count_up(3)
    print(type(g).__name__)          # generator  (no code ran yet)
    print(list(count_up(3)))         # [0, 1, 2]  (now it runs, lazily)
