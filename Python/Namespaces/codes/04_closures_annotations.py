# --- 04_closures_annotations.py ---
"""
Function Closures and Annotation Scopes

This file demonstrates Python's closure mechanism and how annotations
are handled in different scopes. It shows how free variables are
captured and how annotations are evaluated.
"""
from typing import Callable, List

def make_counter(start: int = 0) -> Callable[[], int]:
    """Creates a counter function with its own private state."""
    count = start
    
    def counter() -> int:
        nonlocal count
        current = count
        count += 1
        return current
    
    return counter

def make_multiplier(factor: float) -> Callable[[float], float]:
    """Creates a function that multiplies its input by a stored factor."""
    # 'factor' is a free variable captured by the closure
    def multiplier(x: float) -> float:
        return x * factor
    
    return multiplier

# Demonstrate closure behavior
print("Closure demonstration:")
counter1 = make_counter(5)
counter2 = make_counter(10)

print(f"Counter 1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter 2: {counter2()}, {counter2()}, {counter2()}")

# Demonstrate multiple closures with the same free variable
print("\nMultiplier demonstration:")
double = make_multiplier(2)
triple = make_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# Demonstrate late binding behavior
def create_functions() -> List[Callable[[], int]]:
    """Demonstrates late binding behavior in closures."""
    functions = []
    for i in range(3):
        def func(captured_i=i):  # Use default argument for early binding
            return captured_i
        functions.append(func)
    return functions

print("\nLate binding demonstration:")
funcs = create_functions()
for f in funcs:
    print(f"Function returns: {f()}")

# Demonstrate annotation scopes
def outer(x: 'TypeVar') -> None:
    y: 'TypeVar'  # Forward reference in annotation
    
    class TypeVar:
        pass
    
    y = TypeVar()  # This refers to the local TypeVar class
    print(f"Type of y: {type(y).__name__}")

print("\nAnnotation scope demonstration:")
outer(None)  # The 'TypeVar' in the annotation is treated as a string