
# 🔹 What is a Dictionary?
# A dictionary is a collection of key-value pairs. Keys must be unique and immutable.

# 🔹 Properties of Dictionary:
# - Unordered (in versions < 3.7), insertion-ordered in Python 3.7+
# - Keys must be unique
# - Keys must be of an immutable type (e.g., string, number, tuple)
# - Mutable: can add, remove, or update elements
# - Indexed by keys, not positions

# 🔹 Creating Dictionaries
details = {
    "name": "Abhishek",
    "age": 21,
    "country": "India"
}

empty_dict = {}  # Empty dictionary

# 🔹 Accessing Values
print(details["name"])        # Direct access
print(details.get("age"))     # Using get() (returns None if key not found)

# 🔹 Adding/Updating Values
details["email"] = "abhishek@example.com"   # Adding new key-value

# Update existing value
details["age"] = 22

# 🔹 Removing Elements
details.pop("country")       # Removes key and returns value
details.popitem()            # Removes the last inserted item (Python 3.7+)
del details["age"]            # Delete specific key

# 🔹 Looping Through Dictionary
for key, value in details.items():
    print(f"{key}: {value}")

# 🔹 Dictionary Methods
print(details.keys())         # Returns a view of keys
print(details.values())       # Returns a view of values
print(details.items())        # Returns a view of key-value pairs

# 🔹 Copying Dictionary
copy_dict = details.copy()     # Shallow copy

# 🔹 Merging Dictionaries
more_info = {"gender": "male", "hobby": "coding"}
details.update(more_info)      # Adds key-values from more_info

# 🔹 Nested Dictionary
student = {
    "name": "Abhishek",
    "marks": {
        "math": 90,
        "physics": 85
    },
    "active": True
}
print(student["marks"]["math"])

# 🔹 Dictionary CRUD Operations
# C - Create
d = {"a": 1, "b": 2}

# R - Read
print(d["a"])

# U - Update
d["b"] = 20

# D - Delete
d.pop("a")

# 🔹 Useful Dictionary Functions
print(len(details))            # Number of items
print("name" in details)       # Check if key exists
print(details.get("name"))     # Safe key access

# 🔹 Dictionary Comprehension
squared = {x: x**2 for x in range(5)}
print(f"Squared dict: {squared}")

# 🔹 When to Use Dictionaries?
# - When you need to associate keys with values
# - Efficient lookups and updates
# - Organize structured data like JSON or configs