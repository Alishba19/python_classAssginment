# -----------------------------
# --------- FROZENSET ---------
# -----------------------------

# Frozenset bilkul set jaisa hota hai, magar immutable (badal nahi sakte).
# Ek baar banane ke baad, aap isme items add, remove ya change nahi kar sakte.
# Jab aap chahte hain ke set accidentally change na ho, tab frozenset use karte hain.

# Frozenset create karna:
fruits = frozenset(['apple', 'banana', 'cherry'])
print("Frozen Set:", fruits)
print("Type:", type(fruits))

# Frozenset mein add ya remove karne ki koshish karna error dega:
# fruits.add("mango")       # AttributeError aayega
# fruits.remove("apple")    # AttributeError aayega

# Frozensets pe set operations jaise union, intersection, difference apply kar sakte hain:

set_a = frozenset([1, 2, 3])
set_b = frozenset([3, 4, 5])

# 1) Union (dono sets ke unique elements):
print("Union (| operator):", set_a | set_b)
print("Union (method):", set_a.union(set_b))

# 2) Intersection (common elements):
print("Intersection (& operator):", set_a & set_b)
print("Intersection (method):", set_a.intersection(set_b))

# 3) Difference (set_a ke items jo set_b mein nahi hain):
print("Difference (- operator):", set_a - set_b)
print("Difference (method):", set_a.difference(set_b))

# 4) Symmetric Difference (jo dono sets mein sirf ek mein hain):
print("Symmetric Difference (^ operator):", set_a ^ set_b)
print("Symmetric Difference (method):", set_a.symmetric_difference(set_b))
