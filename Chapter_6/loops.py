
# 🔹 Why Use Loops?
# Loops help in executing a block of code multiple times.
# Python has two primary types of loops: for and while.

# 🔹 for Loop
# Used to iterate over a sequence (list, tuple, dictionary, string, range, etc.)

# Example: loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example: loop using range()
for i in range(5):
    print("Number:", i)

# Using range(start, stop, step)
for i in range(1, 10, 2):
    print("Odd Number:", i)

# 🔹 while Loop
# Repeats as long as a condition is True

count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# 🔹 Loop Control Statements
# break   - exit the loop prematurely
# continue - skip current iteration
# pass    - does nothing, just a placeholder

# break example
for number in range(10):
    if number == 5:
        break
    print("Break Example:", number)

# continue example
for number in range(5):
    if number == 2:
        continue
    print("Continue Example:", number)

# pass example
for i in range(3):
    pass  # Placeholder for future code

# 🔹 Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 🔹 else with Loops
# The else block runs if the loop finishes normally (no break)

for i in range(3):
    print(i)
else:
    print("Loop completed!")

# 🔹 Looping Over a Dictionary
student = {"name": "Abhishek", "age": 21}
for key, value in student.items():
    print(f"{key}: {value}")



# 🔹 Summary:
# - Use for loop when you know the number of iterations
# - Use while loop when repeating until a condition is met
# - Use break, continue, pass to control loop behavior
# - Use zip, enumerate, comprehensions for cleaner advanced code
# - Loops can have an optional else block