# --- 03_class_namespaces.py ---
"""
Class and Instance Namespaces

This file demonstrates how Python handles namespaces in classes,
showing the difference between class variables (shared by all instances)
and instance variables (unique to each instance).
"""

class Dog:
    # Class variable - shared by all instances
    species = "Canis familiaris"
    
    # Class variable containing a mutable object (for demonstration)
    tricks = []  # Shared by all dogs!
    
    def __init__(self, name):
        # Instance variables - unique to each instance
        self.name = name
        self.individual_tricks = []  # Better - each dog has its own list
    
    def add_shared_trick(self, trick):
        # Modifies the class variable (affects all dogs)
        Dog.tricks.append(trick)
    
    def add_individual_trick(self, trick):
        # Modifies the instance variable (affects only this dog)
        self.individual_tricks.append(trick)

# Create two dogs
print("Creating two dogs...\n")
fido = Dog("Fido")
buddy = Dog("Buddy")

# Demonstrate class variable sharing
print("Class variable demonstration:")
print(f"Fido's species: {fido.species}")
print(f"Buddy's species: {buddy.species}")

# Change the class variable
Dog.species = "Canis lupus familiaris"
print("\nAfter changing class variable:")
print(f"Fido's species: {fido.species}")
print(f"Buddy's species: {buddy.species}")

# Demonstrate instance variable independence
print("\nInstance variable demonstration:")
print(f"Fido's name: {fido.name}")
print(f"Buddy's name: {buddy.name}")

# Demonstrate the difference with mutable objects
print("\nShared tricks list (class variable):")
fido.add_shared_trick("roll over")
print(f"Fido's tricks: {Dog.tricks}")
print(f"Buddy's tricks: {buddy.tricks}  # Same list!")

print("\nIndividual tricks lists (instance variables):")
fido.add_individual_trick("play dead")
buddy.add_individual_trick("fetch")
print(f"Fido's individual tricks: {fido.individual_tricks}")
print(f"Buddy's individual tricks: {buddy.individual_tricks}")

# Demonstrate attribute lookup order
print("\nAttribute lookup demonstration:")
buddy.species = "Changed for buddy"  # Creates a new instance variable
print(f"Fido's species (from class): {fido.species}")
print(f"Buddy's species (from instance): {buddy.species}")
print(f"Class species attribute: {Dog.species}")