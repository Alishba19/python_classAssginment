# ------------TUPLES-------------


# Tuples lists ki tarah hotay hain, lekin ye change nahi kiye ja sakte (immutable).
# Tuple items round brackets ( ) mein likhe jate hain.
# Order fix hota hai, duplicates allowed hain, lekin items update, add ya remove nahi kiye ja sakte.

# --------- Tuple kyun use karein? -----------
# Jab data fixed rehna ho, taki koi usay galti se change na kare.
# Tuples lists se tez aur memory efficient hotay hain.

fruits = ("Apple", "Mango", "Banana", "Cherry", "Melon")
print(fruits)

print(len(fruits))  # Tuple mein total items ki tadaad batata hai

# Tuple Indexing: Items ko index se access karte hain, pehla item index 0 hota hai
print(fruits[0])    # Pehla item
print(fruits[-1])   # Aakhri item (negative indexing)

# Tuple Slicing: Index range se specific items ko access karna
print(fruits[1:4])  # Index 1 se 3 tak ke items (4 exclude hai)

# Count: Kisi item ki tuple mein kitni dafa presence hai
print(fruits.count("Apple"))

# Index: Kisi item ka index position batata hai
print(fruits.index("Cherry"))

# Tuple ko list mein convert kar ke change kar sakte hain
fruits_list = list(fruits)
fruits_list.append("Orange")
print("List banane ke baad aur 'Orange' add karne ke baad:", fruits_list)

# Nested Tuple: Tuple ke andar ek aur tuple
nested = ("Fruit", ("Apple", "Banana"))
print(nested)

# Single Item Tuple: Single item tuple banane ke liye comma zaroori hai
single = ("Apple",)
print(type(single))   # Output: <class 'tuple'>
