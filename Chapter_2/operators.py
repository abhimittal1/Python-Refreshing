"""
Python operators are symbols that perform operations on values and variables. 
These include arithmetic, assignment, comparison, logical, identity, and membership operators.

"""
# Arithmetic Operators
x = 10
y = 3
print(x + y)  # Addition: 13
print(x - y)  # Subtraction: 7
print(x * y)  # Multiplication: 30
print(x / y)  # Division: 3.333...
print(x // y) # Floor Division: 3
print(x % y)  # Modulus: 1
print(x ** y) # Exponentiation: 1000


# Assignment Operators
x = 5
x += 3 # Equivalent to x = x + 3
print(x)  # Output: 8

x -= 2 # Equivalent to x = x - 2
print(x)  # Output: 6

x *= 4 # Equivalent to x = x * 4
print(x)  # Output: 24

x /= 3 # Equivalent to x = x / 3
print(x)  # Output: 8.0

x %= 5 # Equivalent to x = x % 5
print(x)  # Output: 3.0

x **= 2 # Equivalent to x = x ** 2
print(x)  # Output: 9.0

x //= 4 # Equivalent to x = x // 4
print(x)  # Output: 2.0


# Comparison Operators
x = 5
y = 10
print(x == y) # Equal: False
print(x != y) # Not equal: True
print(x > y)  # Greater than: False
print(x < y)  # Less than: True
print(x >= y) # Greater than or equal to: False
print(x <= y) # Less than or equal to: True

# Logical Operators

x = True
y = False
print(x and y) # Logical AND: False
print(x or y)  # Logical OR: True
print(not x)  # Logical NOT: False

# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)    # False
print(x is z)    # True
print(x is not y) # True
print(x is not z) # False

# Membership Operators
x = [1, 2, 3]
print(1 in x)    # True
print(4 in x)    # False
print(1 not in x) # False
print(4 not in x) # True