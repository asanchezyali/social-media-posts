from contextlib import suppress, redirect_stdout
import io

# Suppress specific exceptions
with suppress(FileNotFoundError):
    # No exception if file doesn't exist
    open('non_existent.txt').read()

# Redirect output
f = io.StringIO()
with redirect_stdout(f):
    print("Hello, world!")
output = f.getvalue()  # Contains "Hello, world!"
print(output)