"""PEP 479 (default since Python 3.7): a StopIteration that bubbles out of a
generator body is converted to RuntimeError. Don't `raise StopIteration` to
stop a generator — just `return`.
Run:  python 08_stopiteration.py
"""


def bad():
    yield 1
    raise StopIteration          # looks like "stop", but PEP 479 turns it into
                                 # a RuntimeError when it escapes the generator


def good():
    yield 1
    return                       # the right way to end a generator


if __name__ == "__main__":
    print("good():", list(good()))       # [1]
    try:
        list(bad())
    except RuntimeError as exc:
        print("bad() ->", type(exc).__name__, "-", exc)
