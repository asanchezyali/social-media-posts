import threading
import time

# Example: Using a semaphore to limit concurrent resource access
class ConnectionPool:
    def __init__(self, max_connections=3):
        self.semaphore = threading.Semaphore(max_connections)
        
    def get_connection(self):
        self.semaphore.acquire()
        return self  # Return a connection object
        
    def release_connection(self):
        self.semaphore.release()
        
    def __enter__(self):
        return self.get_connection()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release_connection()

# Example usage
def worker(pool, worker_id):
    with pool:
        print(f"Worker {worker_id}: Acquired connection")
        time.sleep(1)  # Simulate work
        print(f"Worker {worker_id}: Released connection")

# Create a connection pool with max 3 connections
pool = ConnectionPool(3)

# Create and start 10 worker threads
threads = []
for i in range(10):
    t = threading.Thread(target=worker, args=(pool, i))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
