# ASSIGNMENT MEMBERSHIP OPERATOR IN PYTHON:
# Used to test whether a value exists in a sequence (like List, Tuple, String, Dictionary).
# Returns True or False.

# -------------------------------------
# IN OPERATOR
fruits = ["Apple","cherry", "Banana"]

print("Apple" in fruits)   # Output: True (Apple is present in the list)
print("Mango" in fruits)  # Output: False (Cherry is not present in the list)

# NOT IN OPERATOR
numbers = [1, 2, 3, 4, 5]

print(1 not in numbers)    # Output: False (1 is present in the list)
print(6 not in numbers)    # Output: True  (6 is not present in the list)

# -------------------------------------
# DICTIONARY EXAMPLE
# Membership works on dictionary keys, not values
my_dict = {
    "name": "ABC",
    "course": "Python"
}

print("XYZ" in my_dict)    # Output: False (It is a value, not a key)
print("name" in my_dict)   # Output: True (Key 'name' exists)
