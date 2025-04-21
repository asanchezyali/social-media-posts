"""
Namespace Collisions in Python

This file demonstrates how namespace collisions can occur
and strategies to avoid them.
"""

# Example 1: Collisions with built-ins
# -----------------------------------------
print("Example 1: Collisions with built-ins")

# Define a variable with the same name as a built-in function
list = [1, 2, 3, 4, 5]
print(f"Our list variable: {list}")

# Now trying to use the built-in list function will fail
try:
    new_list = list("abcde")  # This will fail
    print(f"New list: {new_list}")
except TypeError as e:
    print(f"Error: {e}")

# Restore the built-in
del list
new_list = list("abcde")  # Now it works
print(f"After restoring built-in: {new_list}")

# Example 2: Import collisions
# -----------------------------------------
print("\nExample 2: Import collisions")

# First scenario - same name from different modules
from math import floor
print(f"math.floor(3.7) = {floor(3.7)}")

# If we import a different function with the same name, it overwrites the first one
from statistics import floor
print(f"statistics.floor(3.7) = {floor(3.7)}")  # This is now statistics.floor

# Solution: Use aliases or full module imports
import math
import statistics
print(f"Using full modules - math.floor(3.7) = {math.floor(3.7)}")
print(f"Using full modules - statistics.floor(3.7) = {statistics.floor(3.7)}")

# Example 3: Class namespace collisions
# -----------------------------------------
print("\nExample 3: Class attribute collisions")

class Parent:
    name = "Parent Class"
    
    def say_hello(self):
        return f"Hello from {self.name}"

class Child(Parent):
    name = "Child Class"  # Overrides the parent's name
    
    def say_hello_to_parent(self):
        # Access parent's attributes using super()
        return f"Hello to {super().name}"

parent = Parent()
child = Child()

print(f"Parent says: {parent.say_hello()}")
print(f"Child says: {child.say_hello()}")  # Uses Child's name attribute
print(f"Child trying to access parent's name: {super(Child, child).name}")  # This works but not recommended
print(f"Better way for child to access parent's name: {Parent.name}")

# Example 4: Using __name__ to avoid collisions in modules
# --------------------------------------------------------
print(f"\nExample 4: Current module name: {__name__}")
print("This is useful for writing code that runs only when the module is executed directly")
print("For example: if __name__ == '__main__': main()")

# Clean up imports to avoid affecting other examples
del floor