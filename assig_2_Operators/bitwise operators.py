# ASSIGNMENT BITWISE OPERATOR IN PYTHON:
# In Python, bitwise operators are used to perform operations on individual bits of binary numbers.
# BITWISE OPERATORS LIST:
# & (AND), | (OR),^ (XOR),~ (NOT),<< (LEFT SHIFT),>> (RIGHT SHIFT)

# & (AND) - Returns 1 if both bits are 1, else returns 0
a = 7   # 0b101
b = 5   # 0b011

print(a & b)      # Output: 1 (0b001)

# | (OR) - Returns 1 if any one bit is 1, else returns 0
print(a | b)      # Output: 7 (0b111)

# ^ (XOR) - Returns 1 if bits are different
print(a ^ b)  # Output: 6 (0b110)

# ~ (NOT) - Inverts all bits (flips 0 to 1 and 1 to 0)
c = 5   # 0b101

print(~c)  # Output: -6 (inverted form)

# << (LEFT SHIFT) - Moves bits to the left (Multiply by 2^n)
d = 3  # 0b11

print(d << 2)  # Output: 12 (0b1100)

# >> (RIGHT SHIFT) - Moves bits to the right (Divide by 2^n)
print(d >> 1)  # Output: 1 (0b1)



