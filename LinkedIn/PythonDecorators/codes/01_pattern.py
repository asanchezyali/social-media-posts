"""A decorator is a function that takes a function and returns a new one.

`@log` above a function is exactly `greet = log(greet)` — nothing more.
Run:  python 01_pattern.py
"""


def log(fn):
    def wrapper(*args, **kwargs):
        print(f"-> calling {fn.__name__}")
        result = fn(*args, **kwargs)
        print(f"<- {fn.__name__} returned {result!r}")
        return result
    return wrapper


@log
def greet(name):
    return f"Hi, {name}"


if __name__ == "__main__":
    greet("Ada")
    # These two lines are equivalent — the @ is just sugar:
    plain = log(greet.__wrapped__ if hasattr(greet, "__wrapped__") else greet)
