import os

# -------- Write Mode --------
# Creates file or overwrites if it exists
with open("mydata.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Learning File Handling in Python.")

print("Data written successfully using write mode.")

# -------- Append Mode --------
# Adds new content without removing old content
with open("mydata.txt", "a") as file:
    file.write("\nThis line is added later.")

print("Data appended successfully.")

# -------- Read Mode --------
# Reads and prints file content
try:
    with open("mydata.txt", "r") as file:
        content = file.read()
        print("\nFile Content:\n", content)
except FileNotFoundError:
    print("File not found!")

# -------- Exclusive Creation --------
# Only creates a new file if it doesn't exist
try:
    with open("newlog.txt", "x") as file:
        file.write("This is a new log file.")
    print("newlog.txt created successfully.")
except FileExistsError:
    print("newlog.txt already exists.")

# -------- Delete File --------
# Optional: Delete a file if it exists
if os.path.exists("oldfile.txt"):
    os.remove("oldfile.txt")
    print("oldfile.txt deleted.")
else:
    print("oldfile.txt does not exist.")

