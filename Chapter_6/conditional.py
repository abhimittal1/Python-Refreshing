# 🔹 What are Conditionals?
# Conditionals are used to execute different blocks of code depending on whether a condition is True or False.

# 🔹 Basic Syntax:
# if condition:
#     block of code
# elif another_condition:
#     block of code
# else:
#     block of code

# 🔹 Example:
age = 20
if age >= 18:
    print("You are an adult.")
elif age > 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# 🔹 Comparison Operators:
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

# 🔹 Logical Operators:
# and  - True if both statements are true
# or   - True if at least one statement is true
# not  - Inverts the result

# Example using logical operators:
x = 5
y = 10
if x < 10 and y > 5:
    print("Both conditions are True")

if x == 5 or y == 2:
    print("At least one condition is True")

if not(x > 10):
    print("x is not greater than 10")

# 🔹 Ternary Conditional Operator
# Syntax: value_if_true if condition else value_if_false

is_logged_in = True
message = "Welcome!" if is_logged_in else "Please log in."
print(message)

# 🔹 Nested if statements
number = 10
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")

# 🔹 Membership Operators:
# in     - True if value is in the sequence
# not in - True if value is not in the sequence

colors = ["red", "green", "blue"]
if "red" in colors:
    print("Red is in the list")

if "yellow" not in colors:
    print("Yellow is not in the list")

# 🔹 Identity Operators:
# is      - True if both variables point to the same object
# is not  - True if they do not

a = [1, 2]
b = a
c = [1, 2]

print(a is b)     # True
print(a is c)     # False
print(a == c)     # True (compares values)

# 🔹 Summary:
# - Use conditionals to control flow
# - Combine conditions with logical operators
# - Use membership and identity checks for clean code
# - Use ternary operator for simple inline decisions

# 🎓 Practice Tip:
# Always use proper indentation (4 spaces is standard in Python)
