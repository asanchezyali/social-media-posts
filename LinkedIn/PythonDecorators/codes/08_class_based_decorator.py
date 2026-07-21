"""When a decorator needs to hold state, a class with __call__ is clearer
than three nested functions.

Here: count how many times a function has been called.
Run:  python 08_class_based_decorator.py
"""
from functools import update_wrapper


class CountCalls:
    def __init__(self, fn):
        self.fn = fn
        self.count = 0
        update_wrapper(self, fn)        # the class-based equivalent of @wraps

    def __call__(self, *a, **k):
        self.count += 1
        print(f"{self.fn.__name__} call #{self.count}")
        return self.fn(*a, **k)


@CountCalls
def ping():
    return "pong"


if __name__ == "__main__":
    ping()
    ping()
    ping()
    print("total calls:", ping.count)   # state lives on the instance
