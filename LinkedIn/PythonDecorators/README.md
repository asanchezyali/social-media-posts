# Python decorators, demystified

A decorator takes a function and returns a new one that runs extra logic around it — logging, timing, caching, access checks — without changing the original code. That's the whole idea. Everything else is detail.

This is the long version of the LinkedIn carousel. Every snippet below has a matching runnable file in [`codes/`](codes); run any of them with `python codes/<file>.py`.

- [1. The pattern](#1-the-pattern)
- [2. functools.wraps](#2-functoolswraps--the-one-you-keep-forgetting)
- [3. Decorators with arguments](#3-decorators-with-arguments--three-layers)
- [4. Stacking order](#4-stacking-order)
- [5. The stdlib already ships decorators](#5-the-stdlib-already-ships-decorators)
- [6. @property](#6-property)
- [7. classmethod vs staticmethod](#7-classmethod-vs-staticmethod)
- [8. Class-based decorators, for state](#8-class-based-decorators-for-state)
- [Common mistakes](#common-mistakes)

---

## 1. The pattern

`@log` above a function is not magic. It's sugar for `greet = log(greet)`.

```python
def log(fn):
    def wrapper(*args, **kwargs):
        print(f"-> {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper

@log
def greet(name):
    return f"Hi, {name}"
```

`log` takes a function and returns `wrapper`. Python then rebinds the name `greet` to that wrapper. The `*args, **kwargs` matter: they let the wrapper forward any signature untouched, so `@log` works on a function with two positional args just as well as one with keyword-only args.

Runnable: [`codes/01_pattern.py`](codes/01_pattern.py).

## 2. functools.wraps — the one you keep forgetting

Wrap a function naively and you overwrite its identity. `add.__name__` becomes `"wrapper"`, `add.__doc__` becomes `None`, and every tool that reads those — your debugger, `help()`, Sphinx, pytest's output — now lies to you.

```python
from functools import wraps

def log(fn):
    @wraps(fn)                 # copies __name__, __doc__, __module__, __wrapped__
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper
```

`@wraps(fn)` copies the metadata from the original onto the wrapper. Add it to every decorator you write — no exceptions. Compare the two versions side by side in [`codes/02_wraps.py`](codes/02_wraps.py):

```
without @wraps: wrapper | None
with    @wraps: sub | Subtract two numbers.
```

## 3. Decorators with arguments — three layers

A decorator that takes its own arguments needs one more level of nesting: the **argument**, then the **function**, then the **wrapper**.

```python
def retry(times):
    def deco(fn):
        def wrapper(*a, **k):
            ...                # can see both `times` and `fn`
        return wrapper
    return deco

@retry(3)
def fetch(): ...
```

Read `@retry(3)` as two steps. First `retry(3)` runs and returns `deco`. Then `deco` decorates `fetch`. Miss a layer — forget to return `deco`, or try to accept `times` and `fn` in the same function — and it breaks in a confusing way, usually a `TypeError` about arguments.

A real, working `retry` with backoff is in [`codes/03_decorator_with_args.py`](codes/03_decorator_with_args.py).

## 4. Stacking order

Stacked decorators apply **bottom-up**: the one nearest the function wraps first.

```python
@bold
@italic
def greet(): ...
# same as: greet = bold(italic(greet))
```

So `italic` runs closest to `greet`, and `bold` wraps the result. Flip the two lines and you flip the output. When order matters (say, a decorator that checks auth and another that caches), this is the difference between caching an authorized result and serving a cached result to an unauthorized caller.

## 5. The stdlib already ships decorators

Before you write a caching or dispatch decorator, check `functools`. Since Python 3.9, `@cache` memoizes a function by its arguments — it's the smaller, faster form of `lru_cache(maxsize=None)`:

```python
from functools import cache

@cache
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
```

`fib(35)` goes from millions of calls to 36, and `fib.cache_info()` reports the hits and misses:

```
CacheInfo(hits=33, misses=36, maxsize=None, currsize=36)
```

Reach for `@lru_cache(maxsize=N)` when you want a *bounded* cache with eviction. Worth knowing from the same module: `cached_property` (compute once per instance), `singledispatch` (function overloading by type), `partial`, and `wraps` itself. See [`codes/04_timer.py`](codes/04_timer.py) for a hand-written timing decorator and [`codes/05_lru_cache.py`](codes/05_lru_cache.py) for the cache.

## 6. @property

`@property` turns a method into a read-only attribute — you read `c.area`, not `c.area()`.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
```

Pair it with a setter to guard writes and keep invariants:

```python
@radius.setter
def radius(self, value):
    if value <= 0:
        raise ValueError("radius must be positive")
    self._radius = value
```

Now `c.radius = -1` raises instead of silently corrupting the object. Full example with validation in [`codes/06_property.py`](codes/06_property.py).

## 7. classmethod vs staticmethod

`@classmethod` receives the class as `cls`; `@staticmethod` receives nothing.

```python
class User:
    @classmethod
    def from_json(cls, data):        # alternate constructor
        return cls(data["name"], data["email"])
    @staticmethod
    def valid(email):                # helper, doesn't touch the class
        return "@" in email
```

Use `classmethod` for alternate constructors (`User.from_json(...)`) — because it gets `cls`, it keeps working correctly in subclasses. Use `staticmethod` for helpers that belong to the class conceptually but need neither the instance nor the class. Runnable: [`codes/07_classmethod_staticmethod.py`](codes/07_classmethod_staticmethod.py).

## 8. Class-based decorators, for state

When a decorator has to remember something across calls — a counter, a rate limit, a config — three nested functions get hard to read. A class with `__call__` is clearer, and the state lives on the instance:

```python
class CountCalls:
    def __init__(self, fn):
        self.fn = fn
        self.count = 0
        update_wrapper(self, fn)     # the class-based @wraps
    def __call__(self, *a, **k):
        self.count += 1
        return self.fn(*a, **k)
```

`update_wrapper(self, fn)` is the class-based equivalent of `@wraps`. Full example: [`codes/08_class_based_decorator.py`](codes/08_class_based_decorator.py).

## Common mistakes

- **No `@wraps`.** Broken `__name__`, lost docstrings, confused tooling. Fixed in ten seconds; costs hours to debug.
- **Confusing definition time with call time.** The decorator body runs *once*, when the function is defined. The `wrapper` runs on *every call*. Put expensive setup in the decorator, not the wrapper.
- **Shared mutable state in the closure.** A `list` or `dict` created in the decorator is shared across every decorated function and every call. That's a feature for a cache, a bug for everything else.
- **Reaching for nested functions when you need state.** If it holds state or config, use a class with `__call__`.

---

## Run the code

```bash
git clone https://github.com/asanchezyali/social-media-posts
cd social-media-posts/LinkedIn/PythonDecorators
python codes/02_wraps.py     # or any other file
```

No dependencies — everything here is the standard library.

Written by **Alejandro Sánchez Yalí** · [asanchezyali.com](https://www.asanchezyali.com)
