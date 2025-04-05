import asyncio
import time
import random


async def fan_out_fan_in_example():
    """
    Demonstrates the fan-out/fan-in pattern:
    1. Fan-out: Split a task into multiple subtasks
    2. Process each subtask concurrently
    3. Fan-in: Collect and combine results
    """

    async def process_chunk(chunk_id, data):
        """Process a chunk of data"""
        print(f"Processing chunk {chunk_id} with {len(data)} items")
        await asyncio.sleep(random.uniform(0.5, 1.5))  # Simulate processing

        # Simulate results (sum of items with processing artifact)
        result = sum(data) * random.uniform(0.9, 1.1)
        print(f"Chunk {chunk_id} processed, result: {result:.2f}")
        return result

    # Create a large dataset
    dataset = [i * 2 for i in range(1000)]

    # 1. Fan-out: Split data into chunks
    chunk_size = 100
    chunks = [dataset[i : i + chunk_size] for i in range(0, len(dataset), chunk_size)]
    print(f"Split dataset into {len(chunks)} chunks of {chunk_size} items each")

    # 2. Process chunks concurrently
    print("\nFanning out processing to multiple tasks...")
    tasks = [process_chunk(i, chunk) for i, chunk in enumerate(chunks)]

    # 3. Fan-in: Gather all results
    print("\nFanning in results...")
    start_time = time.time()
    results = await asyncio.gather(*tasks)
    end_time = time.time()

    # Combine results (in this case, take the average)
    final_result = sum(results) / len(results)

    print(f"\nAll chunks processed in {end_time - start_time:.2f} seconds")
    print(f"Final result (average): {final_result:.2f}")


# Run the example
if __name__ == "__main__":
    asyncio.run(fan_out_fan_in_example())

# Split dataset into 10 chunks of 100 items each

# Fanning out processing to multiple tasks...

# Fanning in results...
# Processing chunk 0 with 100 items
# Processing chunk 1 with 100 items
# Processing chunk 2 with 100 items
# Processing chunk 3 with 100 items
# Processing chunk 4 with 100 items
# Processing chunk 5 with 100 items
# Processing chunk 6 with 100 items
# Processing chunk 7 with 100 items
# Processing chunk 8 with 100 items
# Processing chunk 9 with 100 items
# Chunk 0 processed, result: 10331.82
# Chunk 5 processed, result: 106947.79
# Chunk 7 processed, result: 162176.67
# Chunk 3 processed, result: 71535.70
# Chunk 9 processed, result: 187058.54
# Chunk 6 processed, result: 117476.36
# Chunk 2 processed, result: 53288.83
# Chunk 1 processed, result: 31235.51
# Chunk 8 processed, result: 160851.37
# Chunk 4 processed, result: 88868.60

# All chunks processed in 1.38 seconds
# Final result (average): 98977.12