import asyncio
import random


class AsyncTaskQueue:
    """A task queue with priority and worker pool for asyncio"""

    def __init__(self, num_workers=3):
        self.queue = asyncio.PriorityQueue()
        self.num_workers = num_workers
        self.workers = []
        self.running = False
        self._task_counter = 0  # Counter to ensure unique comparison

    async def add_task(self, task_func, priority=0):
        """Add a task to the queue with priority (lower is higher)

        Args:
            task_func: A callable that returns a coroutine (not a coroutine object itself)
            priority: Priority value (lower is higher priority)
        """
        # Increment counter to ensure FIFO behavior for same priority tasks
        self._task_counter += 1
        # Store priority, counter, and task function (not coroutine)
        await self.queue.put((priority, self._task_counter, task_func))

    async def worker(self, worker_id):
        """Worker that processes tasks from the queue"""
        while self.running:
            try:
                # Get a task from the queue
                priority, task_id, task_func = await self.queue.get()

                try:
                    print(
                        f"Worker {worker_id}: Processing task {task_id} with priority {priority}"
                    )
                    # Execute the task function to get the coroutine, then await it
                    result = await task_func()
                    print(
                        f"Worker {worker_id}: Task {task_id} completed with result: {result}"
                    )
                except asyncio.CancelledError:
                    # Handle cancellation properly
                    self.queue.task_done()
                    raise  # Re-raise to propagate cancellation
                except Exception as e:
                    print(f"Worker {worker_id}: Task {task_id} failed with error: {e}")
                finally:
                    # Mark task as done
                    self.queue.task_done()
            except asyncio.CancelledError:
                # Don't call task_done() here as no task was retrieved
                break

    async def start(self):
        """Start the worker pool"""
        self.running = True
        self.workers = [
            asyncio.create_task(self.worker(i)) for i in range(self.num_workers)
        ]

    async def stop(self):
        """Stop the worker pool"""
        self.running = False

        # Give a small timeout for queue to process remaining tasks
        try:
            # Wait for all tasks to complete with a timeout
            await asyncio.wait_for(self.queue.join(), timeout=5.0)
            print("All tasks processed successfully")
        except asyncio.TimeoutError:
            print("Timed out waiting for tasks to complete")

        # Cancel all workers
        for worker in self.workers:
            worker.cancel()

        # Wait for all workers to complete cancellation
        await asyncio.gather(*self.workers, return_exceptions=True)


# Example task implementations
def create_data_processing_task(task_id, duration):
    """Creates a data processing task (returns a task function)"""

    async def _task():
        await asyncio.sleep(duration)  # Simulate work
        return f"Data for task {task_id} processed"

    return _task


async def demo_task_queue():
    # Create a task queue
    task_queue = AsyncTaskQueue(num_workers=3)

    # Start the worker pool
    await task_queue.start()

    try:
        # Add tasks with different priorities
        for i in range(10):
            priority = random.randint(1, 3)  # 1=high, 3=low priority
            duration = random.uniform(0.5, 1.0)

            # Create a task function (not a coroutine) and add it to the queue
            task = create_data_processing_task(i, duration)
            await task_queue.add_task(task, priority)

            print(f"Added Task {i} with priority {priority}")

            # Small delay between adding tasks to better visualize execution
            await asyncio.sleep(0.1)
    finally:
        # Wait for all tasks to complete and stop the worker pool
        await task_queue.stop()
        print("Worker pool stopped")


# Run the demo
if __name__ == "__main__":
    asyncio.run(demo_task_queue())

# Output:
# Added Task 0 with priority 2
# Worker 0: Processing task 1 with priority 2
# Added Task 1 with priority 2
# Worker 1: Processing task 2 with priority 2
# Added Task 2 with priority 3
# Worker 2: Processing task 3 with priority 3
# Added Task 3 with priority 1
# Added Task 4 with priority 1
# Added Task 5 with priority 3
# Added Task 6 with priority 2
# Worker 1: Task 2 completed with result: Data for task 1 processed
# Worker 1: Processing task 4 with priority 1
# Added Task 7 with priority 2
# Added Task 8 with priority 2
# Worker 0: Task 1 completed with result: Data for task 0 processed
# Worker 0: Processing task 5 with priority 1
# Added Task 9 with priority 2
# Worker 2: Task 3 completed with result: Data for task 2 processed
# Worker 0: Task 5 completed with result: Data for task 4 processed
# Worker 1: Task 4 completed with result: Data for task 3 processed
# Timed out waiting for tasks to complete
# Worker pool stopped
