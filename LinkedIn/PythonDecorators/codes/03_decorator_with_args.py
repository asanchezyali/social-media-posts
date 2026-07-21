"""A decorator that takes arguments needs THREE layers:
   the argument -> the function -> the wrapper.

`@retry(3)` first calls retry(3), and the returned `deco` decorates fetch.
Run:  python 03_decorator_with_args.py
"""
import time
from functools import wraps


def retry(times, delay=0.0):
    def deco(fn):
        @wraps(fn)
        def wrapper(*a, **k):
            last = None
            for attempt in range(1, times + 1):
                try:
                    return fn(*a, **k)
                except Exception as exc:         # noqa: BLE001 (demo)
                    last = exc
                    print(f"  attempt {attempt} failed: {exc}")
                    time.sleep(delay)
            raise last
        return wrapper
    return deco


_calls = {"n": 0}


@retry(3)
def flaky():
    _calls["n"] += 1
    if _calls["n"] < 3:
        raise ValueError("boom")
    return "ok"


if __name__ == "__main__":
    print("result:", flaky())   # succeeds on the 3rd attempt
