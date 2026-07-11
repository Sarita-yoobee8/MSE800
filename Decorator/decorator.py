# Import print() function from Python 3 (needed only for Python 2 compatibility)
from __future__ import print_function

# Create an empty dictionary to store registered functions and classes
registry = {}

# Decorator function
def register(obj):
    # Store the function or class in the registry dictionary
    # The key is the object's name (e.g., "spam", "ham", "Eggs")
    registry[obj.__name__] = obj

    # Return the original object (no wrapper function is created)
    return obj


# Register the function 'spam'
@register
def spam(x):
    # Return the square of x
    return x ** 2


# Register the function 'ham'
@register
def ham(x):
    # Return the cube of x
    return x ** 3


# Register the class 'Eggs'
@register
class Eggs:

    # Constructor
    def __init__(self, x):
        # Store x raised to the power of 4
        self.data = x ** 4

    # String representation of the object
    def __str__(self):
        return str(self.data)


# -----------------------------
# Print all registered objects
# -----------------------------
print("Registry:")

for name in registry:
    # Display the name, object, and object type
    print(name, "=>", registry[name], type(registry[name]))


# -----------------------------
# Manual function/class calls
# -----------------------------
print("\nManual calls:")

# Call spam() directly
print(spam(2))          # Output: 4

# Call ham() directly
print(ham(2))           # Output: 8

# Create an object of Eggs
X = Eggs(2)

# Print the object (calls __str__())
print(X)                # Output: 16


# -----------------------------
# Call objects from registry
# -----------------------------
print("\nRegistry calls:")

for name in registry:
    # Call each registered object using the value stored in the dictionary
    # For functions: spam(2), ham(2)
    # For class: Eggs(2)
    print(name, "=>", registry[name](2))