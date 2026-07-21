"""`yield from` yields every value of a sub-iterable (and passes back its return
value). Since Python 3.3 (PEP 380) it replaces the manual re-yield loop.
Run:  python 06_yieldfrom.py
"""


def chain(*iterables):
    for it in iterables:
        yield from it            # instead of: for x in it: yield x


def countdown(n):
    yield from range(n, 0, -1)
    return "liftoff"             # becomes StopIteration.value


if __name__ == "__main__":
    print(list(chain([1, 2], (3, 4), "ab")))     # [1, 2, 3, 4, 'a', 'b']
    print(list(countdown(3)))                    # [3, 2, 1]
