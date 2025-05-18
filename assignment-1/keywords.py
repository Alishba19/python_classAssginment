import keyword

# printing all keywords at once using "kwlist"
print("The list of Python keywords is:")
print(keyword.kwlist)

# ------------------------------------------
# 🔹 Operator Keywords: and, or, not, in, is
# ------------------------------------------

# 1. and → dono conditions true honi chahiye
a = 10
b = 5
if a > 0 and b < 10:
    print("Both conditions are True")

# 2. or → ek bhi condition true ho to chalega
if a > 0 or b > 10:
    print("At least one condition is True")

# 3. not → result ko ulta karta hai
is_valid = False
print(not is_valid)  # True

# 4. in → check karta hai item kisi list ya string mein hai ya nahi
names = ["Ali", "Sara", "Zara"]
print("Ali" in names)     # True
print("Ahmed" in names)   # False

# 5. is → check karta hai dono variables same object ko point kar rahe hain ya nahi
x = 5
y = 5
print(x is y)  # True

# ------------------------------------------
# 🔹 Conditional Keywords: if, elif, else
# ------------------------------------------

# 6. if → condition check karta hai
marks = 80
if marks > 50:
    print("Pass")

# 7. elif → multiple conditions ke liye
if marks > 90:
    print("Grade A")
elif marks > 75:
    print("Grade B")
elif marks > 60:
    print("Grade C")

# 8. else → jab koi bhi condition true na ho
if marks > 90:
    print("Grade A")
else:
    print("Below A")

# ------------------------------------------
# 🔹 Loop/Iteration Keywords: for, while, break, continue, pass
# ------------------------------------------

# 9. for → list ya range ke upar loop
for i in range(3):
    print("Index:", i)

# 10. while → condition ke sath loop
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# 11. break → loop ko turant roknay ke liye
for i in range(5):
    if i == 2:
        break
    print(i)

# 12. continue → current iteration skip karta hai
for i in range(5):
    if i == 2:
        continue
    print(i)

# 13. pass → empty block ke liye placeholder
def todo_function():
    pass  # abhi implement nahi kiya

# ------------------------------------------
# 🔹 Structure Keywords: def, return, class, lambda
# ------------------------------------------

# 14. def → function define karta hai
def welcome():
    print("Welcome to Python!")
welcome()

# 15. return → function se value wapas bhejta hai
def square(n):
    return n * n
print(square(4))

# 16. class → class banata hai (blueprint for object)
class Car:
    brand = "Toyota"
    year = 2022

my_car = Car()
print(my_car.brand)

# 17. lambda → chhoti anonymous function (ek line ka)
multiply = lambda x, y: x * y
print(multiply(3, 4))