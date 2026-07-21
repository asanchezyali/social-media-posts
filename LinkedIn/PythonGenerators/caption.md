Python generators, one value at a time — how `yield` turns a function into a lazy stream, and lets you process data that would never fit in memory. 🐍

A function with a `yield` doesn't return a value; it returns a generator — an iterator that produces values lazily, one at a time, only when something pulls them. It never builds the whole sequence. That single idea is why generators handle streams, huge files, and infinite sequences in constant memory.

What's actually worth knowing:

01 · `yield` freezes the function (locals + position) and resumes on the next pull. A generator is exhausted after one pass — iterate it twice and the second loop sees nothing.
02 · Generator expressions: swap `[ ]` for `( )` and a 400 MB list becomes a ~200-byte generator. Same syntax, wildly different memory.
03 · Pipelines: chain generators and one item flows through the whole chain per pull — grep a 10 GB log holding one line at a time.
04 · Infinite is fine: `while True: yield` is safe because it's lazy; bound it with `islice` or `takewhile`.
05 · `yield from` delegates to a sub-generator (PEP 380) and wires up send/throw/return for free.
06 · `itertools` is the lazy toolkit. Two people miss: `pairwise` (3.10) and `batched` (3.12) — lazy, C-fast, better than index loops.

The gotcha that bites: since Python 3.7 (PEP 479), a `StopIteration` that escapes a generator becomes a `RuntimeError`. Don't `raise StopIteration` to stop — just `return`.

Full write-up + eight runnable, dependency-free examples on GitHub (verified against the official docs) — scan the QR or grab it here:
https://github.com/asanchezyali/social-media-posts/tree/main/LinkedIn/PythonGenerators

What do you reach for more — a list comprehension or a generator? 👇

#python #softwaredevelopment #programming #backend #cleancode #pythontips #dataengineering #itertools #memory #coding
