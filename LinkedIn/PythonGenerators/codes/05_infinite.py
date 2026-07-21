"""A generator can run forever because it's lazy; bound it with islice or
takewhile. itertools.count is the stdlib infinite counter.
Run:  python 05_infinite.py
"""
from itertools import count, islice, takewhile


def naturals():
    n = 0
    while True:            # infinite, but safe: nothing runs until pulled
        yield n
        n += 1


if __name__ == "__main__":
    print(list(islice(naturals(), 5)))            # [0, 1, 2, 3, 4]
    print(list(islice(count(10, 2), 3)))          # [10, 12, 14]
    print(list(takewhile(lambda x: x < 20, count(0, 5))))  # [0, 5, 10, 15]
