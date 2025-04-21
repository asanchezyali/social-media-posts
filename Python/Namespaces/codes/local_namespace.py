"""
Local Namespace in Python

This file demonstrates the behavior and properties of local namespaces,
which are created for functions, methods, and classes.
"""

# Global variables for comparison
x = "global x"
y = "global y"

def basic_local_demo():
    """Demonstrate basic local variable behavior."""
    # Local variables are created within the function
    x = "local x"  # This shadows the global x
    z = "local z"  # This only exists in this function
    
    print("\nBasic local namespace demo:")
    print(f"x inside function: {x}")  # Will print "local x"
    print(f"y from global: {y}")      # Can access global y
    print(f"z inside function: {z}")  # Local variable
    
    # Every function call creates a new local namespace
    for i in range(3):
        counter = i  # New 'counter' for each iteration
        print(f"Loop iteration {i}, counter = {counter}")
    
    # Once we exit the loop, counter still exists in the function's local namespace
    print(f"Counter after loop: {counter}")

def nested_functions_demo():
    """Demonstrate nested function local namespaces."""
    outer_var = "I'm in the outer function"
    
    def inner_function():
        inner_var = "I'm in the inner function"
        print("\nInner function namespace:")
        print(f"inner_var: {inner_var}")
        print(f"outer_var: {outer_var}")  # Can access the enclosing scope
        print(f"Global x: {x}")           # Can access the global scope too
    
    print("\nOuter function namespace:")
    print(f"outer_var: {outer_var}")
    # print(f"inner_var: {inner_var}")  # This would fail - inner_var doesn't exist here
    
    # Call the inner function
    inner_function()

def local_vs_global():
    """Demonstrate the difference between local and global variables with the same name."""
    x = "local x within local_vs_global"
    
    print("\nLocal vs Global:")
    print(f"Local x: {x}")
    # Access the global variable through the globals() function
    print(f"Global x: {globals()['x']}")

def function_arguments():
    """Demonstrate how function parameters become part of the local namespace."""
    def greet(name, greeting="Hello"):
        # name and greeting are part of the local namespace
        message = f"{greeting}, {name}!"
        print(message)
    
    print("\nFunction arguments demo:")
    greet("Alice")
    greet("Bob", "Welcome")
    
    # The parameters don't exist outside the function
    # print(name)  # This would fail

def dynamic_locals():
    """Demonstrate inspection and manipulation of the local namespace."""
    a = 100
    b = 200
    
    print("\nDynamic locals demo:")
    print(f"Local namespace contains: {locals().keys()}")
    
    # Get access to a local variable by name
    var_name = "a"
    print(f"Value of {var_name}: {locals()[var_name]}")
    
    # Changing locals() may not affect actual local variables in CPython
    locals()[var_name] = 999
    print(f"After modifying locals(), a = {a}")  # May still be 100!
    
    # Direct assignment works
    a = 999
    print(f"After direct assignment, a = {a}")

def class_namespaces():
    """Demonstrate class and instance namespaces."""
    class Person:
        species = "Homo sapiens"  # Class variable
        
        def __init__(self, name, age):
            self.name = name  # Instance variable
            self.age = age    # Instance variable
        
        def greet(self):
            # Local variable within the method
            message = f"Hello, my name is {self.name}"
            return message
    
    print("\nClass namespace demo:")
    # Create two instances
    alice = Person("Alice", 30)
    bob = Person("Bob", 25)
    
    # Class variables are shared
    print(f"Person.species: {Person.species}")
    print(f"alice.species: {alice.species}")
    print(f"bob.species: {bob.species}")
    
    # Instance variables are unique to each instance
    print(f"alice.name: {alice.name}")
    print(f"bob.name: {bob.name}")
    
    # Call a method (creates a new local namespace)
    print(alice.greet())

def scope_confusion():
    """Demonstrate a common pitfall with local variables."""
    x = 10
    
    def inner():
        print("\nScope confusion demo:")
        try:
            # This tries to print x first, then increment it
            # But Python sees the later assignment and makes x local to inner()
            print(f"x is: {x}")  # This will fail
            x += 1            # This makes x a local variable
        except UnboundLocalError as e:
            print(f"Error: {e}")
        
        # Fix: use global or nonlocal declaration before using the variable
        print("Using global to fix the issue:")
        global x
        print(f"Global x is: {x}")
        x += 1
        print(f"After increment: {x}")
    
    inner()

def comprehension_variables():
    """Demonstrate scope of variables in comprehensions (Python 3 behavior)."""
    print("\nComprehension variables demo:")
    
    # In Python 3, comprehension variables don't leak
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(f"Squares: {squares}")
    
    # In Python 3, 'n' does not leak into the enclosing scope
    try:
        print(f"Value of n after comprehension: {n}")
    except NameError as e:
        print(f"Error: {e} (n does not leak in Python 3)")
    
    # But for loops do leak their variables
    for n in numbers:
        pass
    print(f"Value of n after for loop: {n}")  # n exists here

# Run our demonstrations
print("Starting local namespaces demonstration...\n")
basic_local_demo()
nested_functions_demo()
local_vs_global()
function_arguments()
dynamic_locals()
class_namespaces()
scope_confusion()
comprehension_variables()

print("\nLocal namespace exploration complete!")