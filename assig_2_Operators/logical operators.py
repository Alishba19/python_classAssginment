#ASSIGNMENT LOGICAL OPERATORS IN PYTHON
# Logical operators are used to combine multiple conditions.
# They return True or False.
# Operators: and, or, not

# ------------------------------------------
# AND OPERATOR
# Returns True only if both conditions are True
a = 10
b = 20

print( a > 5 and b > 15)  # Output: True (Both conditions are True)

# ------------------------------------------
# OR OPERATOR
# Returns True if at least one condition is True
a = 10
b = 5

print( a > 15 or b > 3)    # Output: True (b > 3 is True)

# ------------------------------------------
# NOT OPERATOR
# Reverses the result: True becomes False, False becomes True
a = 10

print( not(a > 5))      # Output: False (a > 5 is True, so not makes it False)
                         