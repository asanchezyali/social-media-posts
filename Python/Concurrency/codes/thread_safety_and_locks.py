import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
        
    def increment(self):
        with self.lock:  # Thread-safe access to shared data
            current = self.value
            time.sleep(0.001)  # Simulate work
            self.value = current + 1
    
    def get_value(self):
        with self.lock:
            return self.value

def increment_counter(counter, count):
    for _ in range(count):
        counter.increment()

# Create a shared counter
counter = Counter()

# Create threads to increment the counter
threads = []
num_threads = 10
increments_per_thread = 100

for _ in range(num_threads):
    t = threading.Thread(
        target=increment_counter, 
        args=(counter, increments_per_thread)
    )
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Check the result
expected = num_threads * increments_per_thread
actual = counter.get_value()
print(f"Expected count: {expected}")
print(f"Actual count: {actual}")
print(f"Thread-safe: {expected == actual}")
