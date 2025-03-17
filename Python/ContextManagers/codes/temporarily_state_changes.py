import os
from contextlib import contextmanager

@contextmanager
def change_directory(path):
    """Temporarily change the working directory."""
    old_dir = os.getcwd()
    try:
        print(f"Changing directory to: {path}")
        os.chdir(path)
        yield  # Give control back to the with block
    finally:
        print(f"Changing back to: {old_dir}")
        os.chdir(old_dir)  # Always restore the original directory

# Code runs with /tmp as working directory
with change_directory("/tmp"):
    print(f"Current directory: {os.getcwd()}")
    # Do some work in the temporary directory
    
# Original directory is restored automatically
print("Back to the original directory")
print(f"Current directory: {os.getcwd()}")