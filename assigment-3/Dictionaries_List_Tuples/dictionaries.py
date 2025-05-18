# ---------------DICTIONARIES---------------

# A dictionary is a collection of key-value pairs. It is:
# Ordered (since Python 3.7): Items are stored in the order they were inserted.
# Mutable: Items can be added, removed, or modified after the dictionary is created.
# Un-indexed: Items are accessed using keys, not indices.
# Without duplicates: Keys must be unique, but values can be duplicated.

# Create a dictionary for student
student ={
    "name": "Ali",
    "roll_no": "003947",
    "age": "20",
    "department": "IT",
    "email": "ali@gmail.com"
    }

# print complete student info
print("Student Info:", student)

# print number of fields
print("Total Fields:", len(student))

# print all keys
print("Fields:", student.keys())

# print all values 
print("values:", student.values())


# Loop through all data
print("\n--- Student Details ---")
for key, value in student.items():
    print(f"{key.capitalize()} : {value}")

# Check if a key exists
print("\nIs 'email' field present?", "email" in student)

# Access specific field
print("Student Name:", student["name"])

# Add new field
student["cgpa"] = 3.8
print("After Adding CGPA:", student)

# Update field
student["age"] = 20
print("After Updating Age:", student)

# Remove a field
student.pop("department")
print("After Removing Department:", student)

# Copy the data
backup = student.copy()
print("Backup Copy:", backup)

# Clear original dictionary
student.clear()
print("After Clearing Student Dictionary:", student)     # Output: {}
