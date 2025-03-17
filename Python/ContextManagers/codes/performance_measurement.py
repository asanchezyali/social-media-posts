import time
from contextlib import contextmanager

@contextmanager
def timer(label):
    """
    A context manager that measures and prints the execution time
    of the code inside the 'with' block.
    
    Parameters:
    - label: A descriptive name for the operation being timed
    """
    # 1. Setup phase: Record the start time
    start = time.time()
    try:
        # 2. Yield control to the with-block
        #    Note: We don't yield a value here since we don't need
        #    to expose any object to the with-block
        yield
    finally:
        # 3. Cleanup phase: Calculate and display elapsed time
        #    This runs even if an exception occurs in the with-block
        end = time.time()
        elapsed = end - start
        print(f"{label}: {elapsed:.4f} seconds")

# Example 1: Basic usage
with timer("Processing data"):
    # Time-consuming operation
    time.sleep(0.5)  # Simulate work with a delay
    
# Example 2: Nested timers for profiling different parts of code
with timer("Complete operation"):
    # First subtask
    with timer("Data loading"):
        time.sleep(0.2)  # Simulate loading data
    
    # Second subtask
    with timer("Processing"):
        time.sleep(0.3)  # Simulate processing
    
    # Third subtask
    with timer("Saving results"):
        time.sleep(0.1)  # Simulate saving

# Output will show:
# Processing data: 0.5002 seconds
#  Data loading: 0.2001 seconds
#  Processing: 0.3002 seconds
#  Saving results: 0.1002 seconds
# Complete operation: 0.6009 seconds