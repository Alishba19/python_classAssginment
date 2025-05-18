# ----------------------------------------
# LOOPS IN PYTHON (for, while, nested for)
# ----------------------------------------

# 1) FOR loop
print("1) FOR loop:")
for i in range(3):
    print("  Hello from for loop:", i)

# 2) WHILE loop
print("\n2) WHILE loop:")
count = 1
while count <= 3:
    print("  Count is:", count)
    count += 1

# 3) NESTED FOR loop
print("\n3) NESTED FOR loop:")
for i in range(1, 3):
    for j in range(1, 3):
        print(f"  i = {i}, j = {j}")