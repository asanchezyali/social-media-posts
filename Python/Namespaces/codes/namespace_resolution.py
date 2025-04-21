"""
Namespace Resolution in Python

This file demonstrates how Python resolves names during execution
using the LEGB (Local, Enclosing, Global, Built-in) rule.
"""

# Built-in namespace
print("= Built-in namespace examples =")
print(f"sum([1, 2, 3]) = {sum([1, 2, 3])}")
print(f"len('hello') = {len('hello')}")

# Global namespace
x = 10
y = 20

def demonstrate_resolution():
    # Accessing global variables (resolution: Global -> Built-in)
    print("\n= Accessing global variables =")
    print(f"x = {x}")  # Finds x in the global scope
    
    # Shadow a global with a local variable
    x = 100  # Creates a new local variable, doesn't affect global x
    print(f"Local x = {x}")
    print(f"Local x is not the same as global x. ID local: {id(x)}, ID global: {id(__builtins__.globals()['x'])}")

def demonstrate_enclosing():
    outer_var = "I'm from the outer function"
    
    def inner_function():
        print("\n= Accessing enclosing variables =")
        print(f"outer_var = {outer_var}")  # Finds variable in the enclosing scope
        
        # Now shadow the enclosing variable
        outer_var = "I'm the local version"  # This will cause UnboundLocalError
        print(f"Local outer_var = {outer_var}")
    
    try:
        inner_function()
    except UnboundLocalError as e:
        print(f"\n= Error when trying to modify enclosing variable without nonlocal =")
        print(f"Error: {e}")
    
    # Fix using nonlocal
    def correct_inner():
        nonlocal outer_var
        print("\n= Using nonlocal to modify enclosing variable =")
        print(f"Original outer_var = {outer_var}")
        outer_var = "Modified from inner function"
        print(f"Modified outer_var = {outer_var}")
    
    correct_inner()
    print(f"After inner function call, outer_var = {outer_var}")


def demonstrate_global():
    print("\n= Using global to modify global variable =")
    print(f"Before modification, global x = {x}")
    
    global x
    x = 500
    print(f"After modification, global x = {x}")


print("Starting namespace resolution demonstration...")
demonstrate_resolution()
demonstrate_enclosing()
demonstrate_global()

print(f"\nFinal value of global x = {x}")

# Name lookup at import time
print("\n= Name lookup at import time =")
print("When you see 'from module import name', Python resolves")
print("'name' in the module's namespace during import.")

# Class namespaces
print("\n= Class namespaces =")

class MyClass:
    class_variable = "I'm shared by all instances"
    
    def __init__(self, instance_var):
        self.instance_variable = instance_var
    
    def method(self):
        # Local variable in the method
        method_var = "I'm local to this method"
        print(f"Inside method: {method_var}")
        print(f"Instance variable: {self.instance_variable}")
        print(f"Class variable: {self.class_variable}")
        # We can also access it through the class
        print(f"Class variable through class: {MyClass.class_variable}")

obj1 = MyClass("object 1")
obj2 = MyClass("object 2")

# Both instances share the class variable
print(f"obj1.class_variable = {obj1.class_variable}")
print(f"obj2.class_variable = {obj2.class_variable}")

# If we modify through the class, it affects all instances
MyClass.class_variable = "Modified class variable"
print(f"After modification, obj1.class_variable = {obj1.class_variable}")

# But if we modify through an instance, it creates an instance variable that shadows the class variable
obj1.class_variable = "obj1's own version"
print(f"obj1.class_variable = {obj1.class_variable}")  # This is now an instance variable
print(f"obj2.class_variable = {obj2.class_variable}")  # This is still the class variable
print(f"MyClass.class_variable = {MyClass.class_variable}")  # The original class variable