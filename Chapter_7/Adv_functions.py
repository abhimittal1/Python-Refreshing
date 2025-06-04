# 🔹 First-Class Functions
# Functions can be assigned to variables, passed as arguments, or returned

def shout(text):
    return text.upper()

print(shout("hello"))

# Assign function to variable
speak = shout
print(speak("python"))

# 🔹 Functions as Arguments

def whisper(text):
    return text.lower()

def greet_func(func):
    print(func("Hello, Abhishek"))

greet_func(shout)
greet_func(whisper)

# 🔹 Returning Functions from Functions

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print("3 x 10 =", times3(10))

# 🔹 Decorators (Modify Function Behavior)

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# 🔹 Built-in Functions (Examples)
print(len("Python"))
print(type(10))
print(max(4, 12, 9))
print(sorted([3, 1, 2]))

# 🔹 Summary:
# - Learn to define, call, and use return values effectively
# - Understand *args, **kwargs for flexible parameters
# - Use lambda for short functions and nested for structured logic
# - Use decorators for reusable wrappers around functions
# - Practice first-class, higher-order, and recursive functions