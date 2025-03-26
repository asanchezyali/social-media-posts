import threading
import time

def worker(name, delay):
    """A simple worker function that demonstrates a thread"""
    print(f"Worker {name}: Starting")
    for i in range(3):
        time.sleep(delay)
        print(f"Worker {name}: Step {i+1}")
    print(f"Worker {name}: Finished")

# Create thread objects
thread1 = threading.Thread(target=worker, args=("A", 0.5))
thread2 = threading.Thread(target=worker, args=("B", 0.8))

# Start the threads
print("Main thread: Starting workers")
thread1.start()
thread2.start()

# Continue with other work in the main thread
print("Main thread: Doing other work")
time.sleep(1)
print("Main thread: Work complete")

# Wait for worker threads to finish
thread1.join()
thread2.join()
print("Main thread: All workers finished")
