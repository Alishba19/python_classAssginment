# INTRODUCTION TO PYTHON
#Python is a high-level, interpreted programming language created by Guido van Rossum and released in 1991.

# DATA TYPES
# Data types specify the type of value a variable holds. Python has several built-in data types.
# Python data types are categorized into two types:
# 1- Mutable Data Type – Values can be changed.
# 2- Immutable Data Type – Values cannot be changed.

# PRIMARY DATA TYPES CATEGORIES
# 1- Numeric Data Types (Immutable): int, float, complex
# 2- Sequence Data Types: list (mutable), tuple (immutable), range
# 3- Set Data Types: set (mutable), frozenset (immutable)
# 4- Mapping Data Types: dict (mutable)
# 5- String Data Types (Immutable)
# 6- Boolean Data Types (Immutable)
# 7- None Data Types

# MOST COMMONLY USED DATA TYPES

#  String (str)
student_name : str = "Ali"
print(student_name)

bio:str = """Name: Ali
Age: 20"""
print(bio)

# Integer (int)
roll_number: int = 101
print(type(roll_number))
print(roll_number)

# Float (float)
percentage: float = 89.5
print(type(percentage))
print(percentage)

# Boolean (bool)
has_passed: bool = True
is_late: bool = False
print(type(has_passed))
print(has_passed)

# List (list)
courses:list[str] =["Math", "physice", "Computer"]
print(type(courses))
print(courses)
print(courses[0])
courses[2] = "Biology"
print(courses)

# Tuple (tuple)
days: tuple = ("Monday", "Tuesday", "Wednesday")
print(type(days))
print(days)
# days[0] = "Sunday"  # Error: tuples are immutable

# Dictionary (dict)
student: dict[str, str] = {
    "Name": "Alishba",
    "Department": "IT"
}
print(type(student))
print(student)

# Set (set)
colors = {"Red", "Blue", "Green"}
print(colors)
colors.add("yellow")
colors.remove("Blue")
print(colors)

# Frozen set (frozenset)
unique_ids = frozenset([101, 102, 103,])
print(unique_ids)

# None 
data = None
print(data)
print(type(data))