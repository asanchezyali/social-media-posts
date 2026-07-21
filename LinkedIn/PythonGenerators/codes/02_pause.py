"""Each `yield` freezes the function (locals + position); the next pull resumes
right after it. A generator is exhausted after one pass.
Run:  python 02_pause.py
"""


def gen():
    print("  start")
    yield 1
    print("  resumed")
    yield 2


if __name__ == "__main__":
    g = gen()
    print("first :", next(g))        # start   -> 1
    print("second:", next(g))        # resumed -> 2

    print("exhausted after one pass:")
    once = gen()
    print("  pass 1:", list(once))   # [1, 2]
    print("  pass 2:", list(once))   # []  -> already spent
