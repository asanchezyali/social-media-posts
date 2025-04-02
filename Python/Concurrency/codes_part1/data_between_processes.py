import multiprocessing as mp

def update_shared_dict(shared_dict, key, value):
    """Update a value in a shared dictionary"""
    shared_dict[key] = value
    print(f"Process {mp.current_process().name} updated shared_dict[{key}] = {value}")

def sum_shared_array(shared_array, result_queue):
    """Calculate sum of a shared array and put result in a queue"""
    total = sum(shared_array)
    result_queue.put(total)
    print(f"Process {mp.current_process().name} calculated sum: {total}")

if __name__ == "__main__":
    # Create a manager to coordinate shared objects
    with mp.Manager() as manager:
        # Create shared objects
        shared_dict = manager.dict()  # Shared dictionary
        shared_array = manager.list(range(10))  # Shared list
        result_queue = manager.Queue()  # Shared queue
        
        # Create processes
        processes = []
        
        # Processes to update the shared dictionary
        for i in range(5):
            p = mp.Process(
                target=update_shared_dict,
                args=(shared_dict, f"key_{i}", i*10)
            )
            processes.append(p)
        
        # Process to calculate sum of shared array
        p = mp.Process(
            target=sum_shared_array,
            args=(shared_array, result_queue)
        )
        processes.append(p)
        
        # Start all processes
        for p in processes:
            p.start()
            
        # Wait for all processes to finish
        for p in processes:
            p.join()
        
        # Retrieve and display results
        print("\nShared dictionary:", dict(shared_dict))
        print("Sum from queue:", result_queue.get())
