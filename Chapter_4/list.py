"""
🔹 What is a List?
A list in Python is a collection of items (elements) that are:
    Ordered (items have an index)
    Mutable (can be changed)
    Can contain mixed data types
"""

# 🔹 Creating Lists
empty_list = []
numbers = [10, 20, 30, 40]
fruits = ["apple", "banana", "mango"]
mixed = [1, "hello", 3.14, False]

# 🔹 Accessing Elements
print(f"First fruit: {fruits[0]}")        # apple
print(f"Last fruit using negative index: {fruits[-1]}")  # mango

# 🔹 Slicing Lists
print(f"Slice from index 1 to 2: {numbers[1:3]}")    # [20, 30]
print(f"Slice from start to 1: {numbers[:2]}")       # [10, 20]
print(f"Slice from index 2 to end: {numbers[2:]}")   # [30, 40]

# 🔹 Modifying Lists
fruits[1] = "orange"       # Change banana to orange
print(f"Modified fruits list: {fruits}")

# 🔹 List Methods
numbers.append(50)         # Add to end
numbers.insert(2, 25)      # Insert at index 2
numbers.remove(30)         # Remove value 30
popped_value = numbers.pop()   # Remove last item
numbers.sort()             # Sort in ascending order --> time complexity is O(n log n) --> mix of insertion and merge sort
numbers.reverse()          # Reverse the list
print(f"Modified numbers list: {numbers}")
print(f"Popped value: {popped_value}")

# 🔹 List Functions
print(f"Length of numbers: {len(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

# 🔹 Looping Through List
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# 🔹 List Comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares from 1 to 5: {squares}")