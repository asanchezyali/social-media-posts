def read_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def grep(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line

def uppercase(lines):
    for line in lines:
        yield line.upper()
        
# Usage
file_lines = read_file('data.txt')
filtered = grep(file_lines, 'python')
result = uppercase(filtered)

# Process results
for line in result:
    print(line)