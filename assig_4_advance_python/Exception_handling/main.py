# -------------- Exception Handling Example 2 --------------
# This example handles file not found and invalid input errors

try:
    # Try to open a file that may not exist
    file = open("data.txt", "r")
    content = file.read()
    print("File Content:", content)

    # Try converting input to integer
    age = int(input("Enter your age: "))
    print("You will be", age + 10, "years old after 10 years.")

except FileNotFoundError:
    print("Error: The file was not found.")

except ValueError:
    print("Error: Please enter a valid number for age.")

else:
    print("Everything went fine!")

finally:
    print("Program finished. Thank you!")
