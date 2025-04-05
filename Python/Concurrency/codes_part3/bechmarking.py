import time
import concurrent.futures


def benchmark(func, data, executor_class, max_workers=None):
    """Benchmark a function using different execution methods"""
    # Sequential execution (baseline)
    start = time.time()
    sequential_result = [func(item) for item in data]
    sequential_time = time.time() - start
    print(f"Sequential: {sequential_time:.4f}s")

    # Concurrent execution
    start = time.time()
    with executor_class(max_workers=max_workers) as executor:
        concurrent_result = list(executor.map(func, data))
    concurrent_time = time.time() - start
    print(f"Concurrent: {concurrent_time:.4f}s")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")


# Example CPU-bound task
def cpu_task(n):
    """CPU-intensive calculation"""
    return sum(i * i for i in range(n * 100000))


# Example I/O-bound task
def io_task(n):
    """I/O-bound operation (simulated)"""
    time.sleep(0.1)  # Simulate I/O delay
    return n * 2


if __name__ == "__main__":
    # This is critical for multiprocessing to work properly
    
    # Data for benchmarking
    data = list(range(1, 9))
    
    # Demo for CPU-bound tasks
    print("CPU-bound task with ProcessPoolExecutor:")
    benchmark(cpu_task, data, concurrent.futures.ProcessPoolExecutor)
    
    # Demo for I/O-bound tasks
    print("\nI/O-bound task with ThreadPoolExecutor:")
    benchmark(io_task, data, concurrent.futures.ThreadPoolExecutor)


# Output:
# CPU-bound task with ProcessPoolExecutor:
# Sequential: 0.1448s
# Concurrent: 0.1072s
# Speedup: 1.35x

# I/O-bound task with ThreadPoolExecutor:
# Sequential: 0.8338s
# Concurrent: 0.1098s
# Speedup: 7.59x