"""Without functools.wraps, the wrapper hides the original function's identity.

Run:  python 02_wraps.py   (compare the two blocks of output)
"""
from functools import wraps


def bad(fn):
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper


def good(fn):
    @wraps(fn)                       # copies __name__, __doc__, __module__, ...
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper


@bad
def add(a, b):
    "Add two numbers."
    return a + b


@good
def sub(a, b):
    "Subtract two numbers."
    return a - b


if __name__ == "__main__":
    print("without @wraps:", add.__name__, "|", add.__doc__)   # wrapper | None
    print("with    @wraps:", sub.__name__, "|", sub.__doc__)   # sub | Subtract...
