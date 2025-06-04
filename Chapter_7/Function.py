# 🔹 What is a Function?
# A function is a block of reusable code that performs a specific task.

# 🔹 Defining a Function

def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()

# 🔹 Function with Parameters

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Abhishek")

# 🔹 Function with Default Parameters

def greet_country(country="India"):
    print(f"Hello from {country}!")

greet_country("USA")
greet_country()

# 🔹 Function with Return Value

def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# 🔹 Multiple Return Values

def calc(a, b):
    return a + b, a - b, a * b, a / b

add_, sub_, mul_, div_ = calc(20, 4)
print("Add:", add_, "Sub:", sub_, "Mul:", mul_, "Div:", div_)

# 🔹 Variable Length Arguments

# *args for variable number of positional arguments
def sum_all(*args):
    return sum(args)

print("Sum of all:", sum_all(1, 2, 3, 4))

# **kwargs for variable number of keyword arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Abhishek", age=21)

# 🔹 Lambda Functions (Anonymous Functions)
add = lambda x, y: x + y
print("Lambda Add:", add(5, 7))

# 🔹 Nested Functions

def outer():
    def inner():
        print("Inner Function")
    inner()

outer()

# 🔹 Recursion (Function calling itself)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 🔹 Scope in Functions
x = 10

def modify():
    global x
    x = 20

modify()
print("Modified x:", x)