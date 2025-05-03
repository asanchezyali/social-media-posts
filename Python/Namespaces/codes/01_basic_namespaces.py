# --- 01_basic_namespaces.py ---
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

# Local namespace in a function with proper global variable handling
def example_function():
    # Declare x as global before using it
    global x
    z = 20  # Local variable
    print("\nLocal namespace inside function:")
    print(f"z = {z}, type: {type(z)}, id: {id(z)}")
    
    # Now we can safely access and modify the global x
    print(f"x from global namespace: {x}")
    x = 30  # This modifies the global x
    print(f"Modified global x: {x}")

# Call the function
print("\nBefore function call:")
print(f"Global x is: {x}")

example_function()

print("\nAfter function call:")
print(f"Global x is now: {x}")  # Will show the modified value