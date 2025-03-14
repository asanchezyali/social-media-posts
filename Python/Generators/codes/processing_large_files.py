# Processing a large file with a list
def process_file_list(filename):
    with open(filename) as f:
        # All lines loaded in memory at once
        return [line.upper() for line in f]

# Processing with a generator
def process_file_generator(filename):
    with open(filename) as f:
        for line in f:
            # Process one line at a time
            yield line.upper()