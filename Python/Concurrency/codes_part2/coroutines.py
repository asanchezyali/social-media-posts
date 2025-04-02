import asyncio
import time

async def say_after(delay, message):
    """Coroutine that waits and then prints a message"""
    await asyncio.sleep(delay)
    print(message)

async def main():
    # Sequential execution
    print("Sequential execution:")
    start = time.time()
    
    await say_after(1, "Hello")
    await say_after(2, "World")
    
    print(f"Sequential took {time.time() - start:.2f} seconds\n")
    
    # Concurrent execution
    print("Concurrent execution:")
    start = time.time()
    
    # Create tasks to run concurrently
    hello_task = asyncio.create_task(say_after(1, "Hello"))
    world_task = asyncio.create_task(say_after(2, "World"))
    
    # Wait for both tasks to complete
    await hello_task
    await world_task
    
    print(f"Concurrent took {time.time() - start:.2f} seconds")

# Run the main coroutine
asyncio.run(main())

# Sequential execution:
# Hello
# World
# Sequential took 3.00 seconds

# Concurrent execution:
# Hello
# World
# Concurrent took 2.00 seconds