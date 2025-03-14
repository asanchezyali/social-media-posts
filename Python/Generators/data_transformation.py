def csv_reader(file_path):
    for line in open(file_path, 'r'):
        yield line.strip().split(',')

def select_columns(data, indices):
    for row in data:
        yield [row[i] for i in indices]

def filter_rows(data, condition_func):
    for row in data:
        if condition_func(row):
            yield row
            
# Usage example
data = csv_reader('large_dataset.csv')
selected = select_columns(data, [0, 2, 3])
filtered = filter_rows(selected, lambda x: float(x[1]) > 100)

for row in filtered:
    print(row)