import multiprocessing as mp
import time
import os

def cpu_bound_task(number):
    """A CPU-intensive function that benefits from parallelization"""
    print(f"Process {os.getpid()} processing {number}")
    # Simulate CPU-intensive calculation
    result = 0
    for i in range(10**7):  # 10 million iterations
        result += i * number
    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Sequential processing
    start_time = time.time()
    sequential_results = [cpu_bound_task(n) for n in numbers]
    sequential_time = time.time() - start_time
    print(f"Sequential processing took {sequential_time:.2f} seconds")
    
    # Parallel processing
    start_time = time.time()
    with mp.Pool(processes=mp.cpu_count()) as pool:
        parallel_results = pool.map(cpu_bound_task, numbers)
    parallel_time = time.time() - start_time
    print(f"Parallel processing took {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")
