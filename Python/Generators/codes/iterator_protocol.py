# Generator functions implement this protocol:
class Counter:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current >= self.max_value:
            raise StopIteration
        self.current += 1
        return self.current

# Example usage
counter = Counter(5)
for number in counter:
    print(number)