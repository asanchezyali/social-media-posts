class SimpleTimer:
    """A simple context manager that measures execution time."""
    
    def __init__(self, name):
        self.name = name
        self.start_time = None
        
    def __enter__(self):
        """
        Called when entering the -with- block.
        Sets up the timer by recording the start time.
        """
        import time
        print(f"Starting timer: {self.name}")
        self.start_time = time.time()
        return self  # This object will be assigned to the variable after -as-
        
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Called when exiting the -with- block (whether normally or due to exception).
        Calculates and displays the elapsed time.
        
        Parameters:
        - exc_type: Type of exception that occurred (or None if no exception)
        - exc_value: The exception object (or None)
        - traceback: The traceback object (or None)
        """
        import time
        elapsed = time.time() - self.start_time
        
        if exc_type is None:
            # No exception occurred
            print(f"Timer {self.name} finished: {elapsed:.4f} seconds")
        else:
            # An exception occurred
            print(f"Timer {self.name} aborted: {elapsed:.4f} seconds")
            print(f"Exception: {exc_type.__name__}: {exc_value}")
            
        # Return False to let exceptions propagate
        # Return True would suppress the exception
        return False

# Using our custom context manager
with SimpleTimer("calculation") as timer:
    print("Performing calculation...")
    # Simulate some work
    total = sum(i**2 for i in range(1000000))
    print(f"Result: {total}")

# The __exit__ method is called automatically when leaving the with block
print("After the with block")