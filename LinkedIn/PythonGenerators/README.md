# Python generators, one value at a time

A function with a `yield` in it doesn't return a value. It returns a **generator** — an iterator that produces values lazily, one at a time, only when something pulls them. It never builds the whole sequence, which is why generators handle streams and data that would never fit in memory.

This is the long version of the LinkedIn article. Every snippet has a runnable file in [`codes/`](codes); run any of them with `python codes/<file>.py` (Python 3.12+ for the `batched` example). Verified against the official docs — itertools, [PEP 380](https://peps.python.org/pep-0380/), and [PEP 479](https://peps.python.org/pep-0479/).

- [1. What a generator is](#1-what-a-generator-is)
- [2. yield pauses and resumes](#2-yield-pauses-and-resumes)
- [3. Generator expressions save memory](#3-generator-expressions-save-memory)
- [4. Pipelines](#4-chaining-generators-into-a-pipeline)
- [5. Infinite streams](#5-infinite-streams-bounded-on-demand)
- [6. yield from](#6-yield-from)
- [7. itertools](#7-itertools-the-lazy-toolkit)
- [8. Sending values in (coroutines)](#8-sending-values-in-coroutines)
- [Common mistakes](#common-mistakes)

---

## 1. What a generator is

```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

Calling `count_up(3)` runs **no code**; it hands back a generator object. The body advances only when the consumer pulls — a `for` loop, `next()`, `sum()`, `list()`. That single idea is the whole point: you hold one value at a time, not the whole list. See [`codes/01_basic.py`](codes/01_basic.py).

## 2. yield pauses and resumes

Each `yield` hands back a value and freezes the function — its locals and its exact position. The next pull resumes right after that `yield`.

```python
def gen():
    print("start");   yield 1
    print("resumed"); yield 2
```

The catch: a generator is **exhausted after one pass**. Iterate it twice and the second loop sees nothing, because the state already ran to the end. Keep a `list` if you truly need to reiterate. Full demo in [`codes/02_pause.py`](codes/02_pause.py).

## 3. Generator expressions save memory

Swap a list comprehension's brackets for parentheses and you get a lazy generator instead of a materialised list.

```python
nums = [x * x for x in range(10_000_000)]   # ~400 MB of int objects in RAM
nums = (x * x for x in range(10_000_000))   # a generator, a couple hundred bytes
total = sum(x * x for x in range(10_000_000))  # streamed, no list built
```

`sys.getsizeof` on the generator reports ~208 bytes regardless of the range. The expression is **lazy**: nothing runs when you write it, so side effects and exceptions are deferred to consumption. Measured in [`codes/03_genexpr.py`](codes/03_genexpr.py).

## 4. Chaining generators into a pipeline

Because each stage is lazy, chained generators pull a **single item** through the whole chain at a time. Memory stays flat no matter how large the input.

```python
from itertools import islice

lines  = (line.rstrip() for line in open("app.log"))
errors = (l for l in lines if "ERROR" in l)
for e in islice(errors, 10):   # only now does anything get read
    print(e)
```

Nothing touches the file until the `for` loop pulls, and it never holds more than one line. That's how you grep a 10 GB log on a laptop. Self-contained version (it writes its own sample log) in [`codes/04_pipeline.py`](codes/04_pipeline.py).

## 5. Infinite streams, bounded on demand

A generator can run forever — `while True: yield` — precisely because it's lazy; you only ever pull what you take.

```python
from itertools import count, islice, takewhile

def naturals():
    n = 0
    while True:
        yield n
        n += 1

list(islice(naturals(), 5))                       # [0, 1, 2, 3, 4]
list(takewhile(lambda x: x < 20, count(0, 5)))    # [0, 5, 10, 15]
```

An eager list of "all the naturals" is impossible; a generator of them is one line. It's the natural model for event streams, retries, and paginated APIs. See [`codes/05_infinite.py`](codes/05_infinite.py).

## 6. yield from

`yield from` yields every value of a sub-iterable and passes back its return value. Since Python 3.3 ([PEP 380](https://peps.python.org/pep-0380/)) it replaces the manual re-yield loop.

```python
def chain(*iterables):
    for it in iterables:
        yield from it          # not: for x in it: yield x
```

`yield from` also wires up `send`, `throw`, and `return` correctly between the outer and inner generator, which the manual loop does not. Example: [`codes/06_yieldfrom.py`](codes/06_yieldfrom.py).

## 7. itertools — the lazy toolkit

Before writing loops over a generator, check `itertools`: `islice`, `chain`, `count`, `groupby`, `takewhile`, `accumulate`. Two newer ones people miss:

```python
from itertools import batched, pairwise

list(batched("ABCDEFG", 3))   # [('A','B','C'), ('D','E','F'), ('G',)]
list(pairwise([1, 2, 3, 4]))  # [(1,2), (2,3), (3,4)]
```

`pairwise` arrived in Python 3.10, `batched` in 3.12 (with a `strict=` flag added in 3.13). Both are lazy and implemented in C, so they beat hand-rolled index loops. See [`codes/07_itertools.py`](codes/07_itertools.py).

## 8. Sending values in (coroutines)

`yield` is also an expression: `x = yield value`. A generator can *receive* data through `.send()`, which makes it a lightweight coroutine.

```python
def running_avg():
    total, n = 0.0, 0
    avg = None
    while True:
        x = yield avg          # receives the value sent in
        total += x; n += 1
        avg = total / n

g = running_avg(); next(g)     # prime it
g.send(10)   # 10.0
g.send(20)   # 15.0
```

This is the classic use before `async`/`await` existed; today you'll mostly reach for `async def` generators for I/O, but `.send()` still shows up in parsers and state machines.

## Common mistakes

- **Reusing an exhausted generator.** It yields nothing the second time. Keep a `list` if you need two passes.
- **`list(gen)` on a huge stream.** That materialises everything and throws away the point — stay lazy end to end.
- **`raise StopIteration` to stop.** Since Python 3.7 ([PEP 479](https://peps.python.org/pep-0479/)), a `StopIteration` that escapes a generator body is converted to `RuntimeError`. Just `return`. Demo: [`codes/08_stopiteration.py`](codes/08_stopiteration.py).
- **Expecting eager errors.** A bug inside the generator surfaces where you *consume* it, not where you define it — a lazy exception can be surprising in a traceback far from the source.

---

## Run the code

```bash
git clone https://github.com/asanchezyali/social-media-posts
cd social-media-posts/LinkedIn/PythonGenerators
python codes/03_genexpr.py     # or any other file
```

No dependencies — everything here is the standard library.

Written by **Alejandro Sánchez Yalí** · [asanchezyali.com](https://www.asanchezyali.com)
