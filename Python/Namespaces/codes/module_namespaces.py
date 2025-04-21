"""
Module Namespaces in Python

This file demonstrates how modules create separate namespaces,
and how to import and use objects from different modules.
"""

# Each module has its own namespace
import math
import random
import datetime as dt

# Different modules can have variables or functions with the same name
# without conflicts, because they exist in separate namespaces

print("Module namespaces:")
print(f"math.pi = {math.pi}")
print(f"sin(30°) = {math.sin(math.radians(30))}")

print(f"\nrandom.random() = {random.random()}")
print(f"random choice from list = {random.choice(['apple', 'banana', 'cherry'])}")

# Using an aliased import
current_time = dt.datetime.now()
print(f"\nCurrent time: {current_time}")

# Importing specific items to the local namespace
from math import sqrt, pow
print(f"\nImported directly: sqrt(16) = {sqrt(16)}")
print(f"Imported directly: pow(2, 3) = {pow(2, 3)}")

# Star imports (generally not recommended as it can lead to namespace pollution)
# but useful for illustration
from random import *
print(f"\nAfter star import: randint(1, 10) = {randint(1, 10)}")

# Python creates a __dict__ attribute for each module
print("\nExamining math module's namespace:")
# Print just a few items to avoid overwhelming output
some_items = list(math.__dict__.items())[:5]
for name, obj in some_items:
    print(f"{name}: {obj}")

# Creating our own module attribute
math.custom_value = "This is added to the math module's namespace"
print(f"\nCustom attribute: {math.custom_value}")

# Note that this doesn't modify the actual math module on disk;
# it only affects this instance in memory