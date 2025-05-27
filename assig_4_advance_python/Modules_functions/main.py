# Import complete module
import math_operations

# Import specific function
from math_operations import multiplyy

# Normal function
def add(x, y):
    return x + y

# Function call
result = add(20, 30)
print("Sum:", result)

# Lambda function
sum_lambda = lambda x, y: x + y
print("Lambda Sum:", sum_lambda(30, 40))

# Lambda in sorting
my_dict = {"apple": 5, "banana": 3, "cherry": 7, "date": 1}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary:", sorted_dict)

# Scope of variable (Local vs Global)
total = 0
def sum_numbers(a, b):
    total = a + b  # Local
    print("Inside Function:", total)

sum_numbers(30, 40)
print("Outside Function:", total)

# Function with *args
def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print("Multiply:", multiply(2, 4, 5))
print("Multiply:", multiply(5, 10))

# Recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Using custom module
print("Module Add:", math_operations.add(20, 35))
print("Module Multiply:", multiplyy(10, 2))
