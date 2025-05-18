# ASSIGNMENT IDENTITY OPERATORS IN PYTHON.
# Identity operators are used to compare the memory location of two objects.
# They return True or False.

# Operators: is, is not

# ---------------------------------------------
# NOTE:
# - Immutable types (str, int, tuple) may share memory if values are the same.
# - Mutable types (list, dict, set) are stored at different memory locations, even if values are same.

# IS OPERATOR
a = "abc"
b = "xyz"
print( a is b)   # Output: False (Different values, different memory)

a = "abc"
b = "abc"
print( a is b)   # Output: True (Same value, same memory location for strings)

# ---------------------------------------------
# IS NOT OPERATOR 
a = ["abc", "xyz"]
b = ["abc", "xyz"]
print( a is b)   # Output: False (Lists are mutable, so different memory location)

# IS NOT OPERATOR 
a = 20
b = 30
print( a is not b)  # Output: True (Different values, different memory)
