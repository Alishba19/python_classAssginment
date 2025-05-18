# -------------SET--------------

# Set aik aisi collection hai jo multiple unique items rakhti hai.
# Sets mein duplicates allow nahi hote.
# Sets unordered hote hain, is liye index se access nahi kar sakte.
# Aap items add ya remove kar sakte hain, magar existing item update nahi kar sakte.

# Basic Set Example:
info = {"Ali", 19, True, 1, False, 0}
print("Set Info:", info)  
# Note: True aur 1 ek jese hain, False aur 0 bhi ek jese, is liye duplicates ignore hote hain.

# Length of Set
print("Set Length:", len(info))

# Add item
info.add("Ayan")
print("After Add:", info)

# Remove item
info.remove("Ali")
print("After Remove:", info)

# Looping through set
for item in info:
    print("Item:", item)

# Clear set
info.clear()
print("After Clear:", info)  # Output: set()

# Empty Set vs Empty Dict
empty_dict = {}
print("Empty dict type:", type(empty_dict))  # <class 'dict'>

empty_set = set()
print("Empty set type:", type(empty_set))    # <class 'set'>


# Set operations example
set1 = {1, 4, 6, 7}
set2 = {3, 4, 5, 8}

print("Set1:", set1)
print("Set2:", set2)

# Union (combined unique items)
print("Union:", set1.union(set2))

# Intersection (common items)
print("Intersection:", set1.intersection(set2))

# Update set1 with intersection
set1.intersection_update(set2)
print("After Intersection Update set1:", set1)

# Symmetric difference (items unique to each set)
print("Symmetric difference:", set1.symmetric_difference(set2))

# Difference (items in set2 not in set1)
print("Difference (set2 - set1):", set2.difference(set1))

# Add and remove items
set1.add(9)
print("After adding 9 to set1:", set1)

set2.discard(2)  # discard does nothing if item not found
print("After discarding 2 from set2:", set2)

# Pop removes random item
set1.pop()
print("After pop from set1:", set1)

# Clear set2
set2.clear()
print("After clear set2:", set2)


# Set relationships
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("Is A subset of B?", A.issubset(B))    # True
print("Is B subset of A?", B.issubset(A))    # False

print("Is A superset of B?", A.issuperset(B))  # False
print("Is B superset of A?", B.issuperset(A))  # True

C = {4, 5, 6}
print("Are A and C disjoint?", A.isdisjoint(C))  # True
