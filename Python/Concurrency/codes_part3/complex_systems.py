import asyncio
import concurrent.futures
import time


def cpu_bound(number):
    """CPU-bound task (runs in a process)"""
    total = sum(i * i for i in range(number))
    return total


def io_bound(number):
    """I/O-bound task (runs in a thread)"""
    time.sleep(1)  # Simulate I/O
    return number * 2


async def main():
    # Create executor pools
    process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=4)
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)

    loop = asyncio.get_running_loop()

    # CPU-bound tasks (run in process pool)
    cpu_numbers = [5_000_000, 10_000_000, 15_000_000, 20_000_000]
    cpu_tasks = [
        loop.run_in_executor(process_pool, cpu_bound, number) for number in cpu_numbers
    ]

    # I/O-bound tasks (run in thread pool)
    io_numbers = list(range(1, 11))
    io_tasks = [
        loop.run_in_executor(thread_pool, io_bound, number) for number in io_numbers
    ]

    # Async I/O-bound tasks (native asyncio)
    async_tasks = [asyncio.sleep(1, result=f"async_{i}") for i in range(5)]

    # Gather all results
    print("Running all tasks concurrently...")
    start = time.time()

    cpu_results = await asyncio.gather(*cpu_tasks)
    io_results = await asyncio.gather(*io_tasks)
    async_results = await asyncio.gather(*async_tasks)

    end = time.time()

    # Show results
    print(f"\nTotal time: {end - start:.2f} seconds")
    print(f"CPU results: {len(cpu_results)} tasks completed")
    print(f"I/O results: {len(io_results)} tasks completed")
    print(f"Async results: {len(async_results)} tasks completed")

    # Clean up
    process_pool.shutdown()
    thread_pool.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

# Running all tasks concurrently...

# Total time: 2.02 seconds
# CPU results: 4 tasks completed
# I/O results: 10 tasks completed
# Async results: 5 tasks completed
