# --- 02_nested_scopes.py ---
"""
Nested Scopes and the nonlocal Keyword

This file demonstrates how Python handles nested function scopes
and the usage of the 'nonlocal' keyword for modifying variables
in outer (but not global) scopes.
"""

def scope_test():
    def do_local():
        spam = "local spam"  # Creates a new local variable

    def do_nonlocal():
        nonlocal spam        # Refers to spam in scope_test
        spam = "nonlocal spam"

    def do_global():
        global spam         # Refers to global spam
        spam = "global spam"

    # Initialize spam in scope_test's scope
    spam = "test spam"
    print("Initial value:", spam)
    
    do_local()
    print("After local assignment:", spam)
    
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    
    do_global()
    print("After global assignment:", spam)

print("Starting scope test\n")
scope_test()
print("\nIn global scope:", spam)  # Will print the global spam value