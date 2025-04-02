import asyncio
import random


async def producer_consumer_example():
    # Create a queue with a maximum size
    queue = asyncio.Queue(maxsize=5)

    async def producer():
        """Produces tasks and adds them to the queue"""
        for i in range(10):
            # Create a task
            task = f"Task-{i}"

            # Put the task in the queue (will wait if queue is full)
            await queue.put(task)
            print(f"Producer: Created {task}")

            # Simulate variable production time
            await asyncio.sleep(random.uniform(0.1, 0.5))

        # Signal end of production
        print("Producer: Done producing")

    async def consumer(name):
        """Consumes tasks from the queue"""
        while True:
            try:
                # Get a task from the queue (will wait if queue is empty)
                task = await queue.get()

                # Check for sentinel value signaling end
                if task is None:
                    print(f"{name}: Received shutdown signal")
                    queue.task_done()
                    break

                print(f"{name}: Processing {task}")

                # Simulate processing time
                await asyncio.sleep(random.uniform(0.2, 0.7))

                print(f"{name}: Completed {task}")

                # Signal task completion
                queue.task_done()

            except asyncio.CancelledError:
                break

    # Start producer and consumer tasks
    producer_task = asyncio.create_task(producer())
    consumer_tasks = [asyncio.create_task(consumer(f"Consumer-{i}")) for i in range(3)]

    # Wait for the producer to finish
    await producer_task

    # Wait for all items to be processed
    await queue.join()

    # Send shutdown signal to all consumers
    for _ in range(len(consumer_tasks)):
        await queue.put(None)

    # Wait for consumers to process shutdown signal
    await asyncio.gather(*consumer_tasks)


# Run the example
if __name__ == "__main__":
    asyncio.run(producer_consumer_example())
