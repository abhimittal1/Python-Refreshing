
# 🔹 What is a Tuple?
# A tuple is like a list but it's immutable (cannot be changed after creation)

# 🔹 Creating Tuples
empty_tuple = ()
single_element = (5,)          # Note the comma
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, False)

# 🔹 Accessing Elements
print(f"First number: {numbers[0]}")
print(f"Last number using negative index: {numbers[-1]}")

# 🔹 Slicing Tuples
print(f"Slice from index 1 to 3: {numbers[1:4]}")
print(f"Slice from start to 2: {numbers[:3]}")
print(f"Slice from index 3 to end: {numbers[3:]}")

# 🔹 Tuple is Immutable
# numbers[0] = 10  # ❌ This will raise an error

# 🔹 Looping Through Tuple
print("Numbers in the tuple:")
for number in numbers:
    print(number)

# 🔹 Tuple Methods
print(f"Count of 2: {numbers.count(2)}")       # How many times 2 appears
print(f"Index of 4: {numbers.index(4)}")       # Position of element 4

# 🔹 Tuple Packing and Unpacking
person = ("Abhishek", 21, "India")
name, age, country = person
print(f"Name: {name}, Age: {age}, Country: {country}")

# 🔹 When to Use Tuples?
# - When your data should not be changed
# - Tuples are slightly faster than lists
# - Useful for fixed data like coordinates, days of week etc.
