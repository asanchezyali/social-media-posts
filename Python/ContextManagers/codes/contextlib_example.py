from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        # Setup code
        f = open(filename, mode)
        yield f  # Yield the resource
    finally:
        # Cleanup code
        f.close()

# Usage
with file_manager('example.txt', 'r') as f:
    content = f.read()