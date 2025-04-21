"""
Basic Namespaces in Python

This file demonstrates the fundamental concept of namespaces in Python.
A namespace is a mapping from names to objects.
"""

# The built-in namespace contains functions like print, len, etc.
print("Built-in namespace example:")
print(f"Type of len function: {type(len)}")
print(f"ID of len function: {id(len)}")

# The global namespace of a module
x = 10
y = "hello"

print("\nGlobal namespace example:")
print(f"x = {x}, type: {type(x)}, id: {id(x)}")
print(f"y = {y}, type: {type(y)}, id: {id(y)}")

# Local namespace in a function
def example_function():
    z = 20  # Local variable
    print("\nLocal namespace inside function:")
    print(f"z = {z}, type: {type(z)}, id: {id(z)}")
    
    # We can access global variables from inside a function
    print(f"x from global namespace: {x}")
    
    # But if we create a local variable with the same name,
    # it shadows the global variable
    x = 30  # This creates a new local variable
    print(f"Local x = {x}, type: {type(x)}, id: {id(x)}")

# Call the function
example_function()

# x in the global namespace is not affected
print("\nAfter function call:")
print(f"Global x is still: {x}")