"""Chained generators form a lazy pipeline: one item is pulled through every
stage at a time, so memory stays flat regardless of input size.
Run:  python 04_pipeline.py
"""
import tempfile
import os
from itertools import islice


def build_sample_log(path, n=1000):
    with open(path, "w") as f:
        for i in range(n):
            level = "ERROR" if i % 7 == 0 else "INFO"
            f.write(f"{level} event {i}\n")


if __name__ == "__main__":
    path = os.path.join(tempfile.gettempdir(), "app.log")
    build_sample_log(path)

    lines = (line.rstrip() for line in open(path))     # lazy
    errors = (l for l in lines if "ERROR" in l)        # lazy
    first = islice(errors, 5)                          # lazy: nothing read yet

    for e in first:                                    # now it pulls
        print(e)
    os.remove(path)
