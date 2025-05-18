# ---------------LIST---------------

# A list is a collection which is:
# Ordered, Mutable (changeable), Allows Duplicates, and Indexed.

# Create a list of student names
students = ["Alishba", "Ali", "Zara", "Hamza"]

# Print the whole list
print("Student List:", students)

# Print specific item by index
print("First Student:", students[0])

# Check total number of students
print("Total Students:", len(students))

# Add a new student at the end
students.append("Usman")
print("After Append:", students)

# Insert a student at specific position
students.insert(2, "Rabia")
print("After Insert at index 2:", students)

# Remove a student
students.remove("Ali")
print("After Remove Ali:", students)

# Sort the list
students.sort()
print("After Sorting:", students)

# Reverse the list
students.reverse()
print("After Reversing:", students)

# Loop through the list
print("\n-- Student Names --")
for name in students:
    print(name)

# Copy the list
student_backup = students.copy()
print("Backup List:", student_backup)

# Clear the list
students.clear()
print("After Clearing:", students)
