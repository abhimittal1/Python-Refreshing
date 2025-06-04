# 🔹 Advanced Looping Techniques

# Enumerate - to get index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Zip - iterate over multiple sequences in parallel
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# List Comprehensions (Compact loops for creating lists)
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Dictionary Comprehensions
cube_dict = {x: x**3 for x in range(5)}
print("Cube Dictionary:", cube_dict)

# Set Comprehensions
unique_lengths = {len(word) for word in ["apple", "banana", "cherry"]}
print("Unique Word Lengths:", unique_lengths)

# Using loops with conditional expressions
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)