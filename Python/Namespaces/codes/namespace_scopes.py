"""
Namespace Scopes in Python

This file demonstrates the LEGB rule for namespace resolution:
L - Local: Variables defined within a function
E - Enclosing: Variables defined in the enclosing function 
G - Global: Variables defined at the top level of a module
B - Built-in: Python's built-in namespace
"""

# Global variable
x = "global x"

def outer_function():
    # Enclosing variable (from inner_function's perspective)
    x = "enclosing x"
    
    def inner_function():
        # Local variable
        x = "local x"
        print(f"Local x in inner_function: {x}")
        
    # Call the inner function
    inner_function()
    print(f"Enclosing x in outer_function: {x}")

# Call the outer function
outer_function()
print(f"Global x: {x}")

# Demonstrating the 'global' keyword
def modify_global():
    global x
    x = "modified global x"
    print(f"Inside modify_global(): {x}")

print("\nBefore calling modify_global():", x)
modify_global()
print("After calling modify_global():", x)

# Demonstrating the 'nonlocal' keyword
def outer():
    y = "outer y"
    
    def inner():
        nonlocal y  # This allows us to modify the enclosing variable
        y = "modified by inner()"
        print(f"Inside inner(): {y}")
    
    print(f"Before calling inner(): {y}")
    inner()
    print(f"After calling inner(): {y}")

print("\nDemonstrating nonlocal:")
outer()

# Accessing built-in namespace
print("\nBuilt-in namespace:")
print(f"Built-in function: {abs(-5)}")

# Try to override a built-in function
abs = lambda x: x * 2
print(f"After overriding: abs(-5) = {abs(-5)}")

# Access original built-in function using __builtins__
print(f"Original abs via __builtins__: {__builtins__.abs(-5)}")

# Clean up by deleting our override
del abs