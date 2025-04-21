"""
Global Namespace in Python

This file demonstrates the behavior and properties of the global namespace,
including how to access and modify global variables.
"""

# Variables in the module scope are in the global namespace
language = "Python"
version = 3.9
features = ["namespaces", "decorators", "generators", "context managers"]

# Print some initial global variables
print("Initial global variables:")
print(f"language = {language}")
print(f"version = {version}")
print(f"features = {features}")

# Function to modify global variables
def modify_globals():
    # Use the global keyword to modify global variables
    global language, version
    
    language = "Python 3"
    version = 3.10
    
    # Adding to a mutable object like a list doesn't require 'global'
    features.append("type hinting")
    
    print("\nInside modify_globals():")
    print(f"language = {language}")
    print(f"version = {version}")
    print(f"features = {features}")

# Function trying to modify global variables without 'global'
def wrong_modification():
    try:
        # This creates a new local variable instead of modifying the global one
        language = "Java"
        print(f"\nInside wrong_modification(), local language = {language}")
        
        # But we can still read the global variables
        print(f"Global version = {version}")
    except UnboundLocalError as e:
        print(f"\nError in wrong_modification(): {e}")

# Function to show global lookup
def check_globals():
    import builtins
    
    print("\nInspecting global namespace:")
    
    # Check if variables exist in globals
    print(f"Is 'language' in globals? {'language' in globals()}")
    print(f"Is 'os' in globals? {'os' in globals()}")
    
    # Dynamically access global variables
    print(f"Global language via globals(): {globals()['language']}")
    
    # Built-ins and global namespace
    print(f"Built-in print function: {builtins.print}")
    print(f"Is built-in 'print' in globals? {'print' in globals()}")

# Demonstrate module-level variables and imports
print("\nImporting modules into global namespace:")

import os  # This adds 'os' to the global namespace
from sys import version_info  # This adds 'version_info' to the global namespace

print(f"os.name = {os.name}")
print(f"version_info = {version_info}")

# Call our functions to demonstrate global variable behavior
modify_globals()
wrong_modification()
check_globals()

# Add a variable to global namespace dynamically
globals()["new_variable"] = "I was added dynamically"
print(f"\nDynamically added variable: {new_variable}")

# Show the relationship between __name__ and the global namespace
print(f"\nCurrent module name: {__name__}")
print(f"Is '__name__' in globals? {'__name__' in globals()}")

# A class defined at the top level becomes part of the global namespace
class GlobalClass:
    class_var = "I'm in a globally defined class"

# The class itself is in the global namespace
print(f"\nIs 'GlobalClass' in globals? {'GlobalClass' in globals()}")
print(f"Accessing class from global: {globals()['GlobalClass'].class_var}")

# Clean up our global namespace example
# In practical code, you should avoid polluting the global namespace
def main():
    """Encapsulate code in a function to avoid global namespace pollution."""
    result = 100 * version
    print(f"\nEncapsulated calculation: {result}")

# Standard practice for scripts
if __name__ == "__main__":
    main()