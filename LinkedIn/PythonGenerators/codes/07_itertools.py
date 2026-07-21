"""itertools is the lazy toolkit for generators. batched (3.12) and pairwise
(3.10) are the two people miss most; both are lazy and C-fast.
Run:  python 07_itertools.py   (needs Python 3.12+ for batched)
"""
from itertools import batched, pairwise, islice, accumulate

if __name__ == "__main__":
    print(list(batched("ABCDEFG", 3)))        # [('A','B','C'), ('D','E','F'), ('G',)]
    print(list(pairwise([1, 2, 3, 4])))       # [(1,2), (2,3), (3,4)]
    print(list(islice(accumulate([1, 2, 3, 4]), 4)))  # running sum: [1, 3, 6, 10]
