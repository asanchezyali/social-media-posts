"""
Namespace Inspection in Python

This file demonstrates how to inspect and explore namespaces in Python
using built-in functions and attributes.
"""

import math
import sys

# 1. Inspecting the global namespace with globals()
# -------------------------------------------------
print("1. Global namespace inspection:")
print("-" * 50)

# Define some variables
x = 100
y = "hello"
z = [1, 2, 3]

# Print some selected elements from globals()
# (Filter out private names for cleaner output)
global_vars = {k: v for k, v in globals().items() if not k.startswith('_')}
print(f"Global namespace contains {len(globals())} items")
print(f"Selected user-defined variables: {global_vars}")

# 2. Inspecting the local namespace with locals()
# -------------------------------------------------
print("\n2. Local namespace inspection:")
print("-" * 50)

def local_inspection():
    a = 10
    b = 20
    
    # In this context, locals() will show only the local variables
    local_vars = locals()
    print(f"Local namespace contains {len(local_vars)} items:")
    for name, value in local_vars.items():
        print(f"  {name} = {value}")
    
    # Modifying locals() directly may not affect actual local variables
    local_vars['a'] = 999
    print(f"After modifying locals() dict, a = {a}")  # May still be 10!

local_inspection()

# 3. Inspecting modules
# -------------------------------------------------
print("\n3. Module namespace inspection:")
print("-" * 50)

# Exploring the math module namespace
print(f"Math module has {len(dir(math))} attributes")
print("Some mathematical constants:")
for name in dir(math):
    # Only print constants (all-uppercase names by convention)
    if name.isupper():
        value = getattr(math, name)
        print(f"  math.{name} = {value}")

# 4. Inspecting the built-in namespace
# -------------------------------------------------
print("\n4. Built-in namespace inspection:")
print("-" * 50)

# Get all built-in functions and objects
builtins = dir(__builtins__)
print(f"Built-in namespace has {len(builtins)} items")
print("Some common built-in functions:")
common_builtins = ['print', 'len', 'str', 'int', 'list', 'dict', 'max', 'min', 'sum']
for name in common_builtins:
    print(f"  {name}: {getattr(__builtins__, name)}")

# 5. Inspecting a class namespace
# -------------------------------------------------
print("\n5. Class namespace inspection:")
print("-" * 50)

class MyClass:
    class_var = "I'm a class variable"
    
    def __init__(self):
        self.instance_var = "I'm an instance variable"
    
    def method(self):
        pass
    
    @classmethod
    def class_method(cls):
        pass
    
    @staticmethod
    def static_method():
        pass

# Inspect class attributes
print("Class attributes:")
class_attrs = {name: value for name, value in MyClass.__dict__.items() 
               if not name.startswith('__')}
for name, value in class_attrs.items():
    print(f"  {name}: {value}")

# Create an instance and inspect its attributes
obj = MyClass()
print("\nInstance attributes:")
instance_attrs = obj.__dict__
for name, value in instance_attrs.items():
    print(f"  {name}: {value}")

# 6. Inspecting the current frame
# -------------------------------------------------
print("\n6. Inspecting the current frame:")
print("-" * 50)

def get_frame_info():
    import inspect
    frame = inspect.currentframe()
    
    # Get the frame's local and global variables
    local_vars = frame.f_locals
    global_vars = frame.f_globals
    
    # Display function name
    print(f"Function name: {frame.f_code.co_name}")
    print(f"Local variables: {list(local_vars.keys())}")
    
    # Always delete the frame reference when done
    del frame

get_frame_info()

# 7. Namespace hierarchy with variable lookups
# -------------------------------------------------
print("\n7. Namespace lookup demonstration:")
print("-" * 50)

var_name = "x"
if var_name in locals():
    print(f"{var_name} found in locals(): {locals()[var_name]}")
elif var_name in globals():
    print(f"{var_name} found in globals(): {globals()[var_name]}")
elif hasattr(__builtins__, var_name):
    print(f"{var_name} found in builtins: {getattr(__builtins__, var_name)}")
else:
    print(f"{var_name} not found in any namespace")