# Without context manager
file = open('data.txt', 'r')
try:
    content = file.read()
finally:
    file.close()

# With context manager
with open('data.txt', 'r') as file:
    content = file.read()
# File is automatically closed