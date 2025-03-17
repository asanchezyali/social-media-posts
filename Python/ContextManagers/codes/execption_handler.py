class ExceptionHandler:
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Handled: {exc_type.__name__}: {exc_val}")
            return True  # Suppress the exception
        return False  # Propagate any exception

# Exception will be suppressed
with ExceptionHandler():
    result = 1 / 0
    print("This won't execute")
print("But this will")  # Execution continues