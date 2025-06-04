# 🔹 What is a Set?
# A set is an unordered collection of unique and immutable elements.

# 🔹 Properties of Set:
# - Unordered: No guaranteed order (no indexing)
# - Unique: Duplicates are automatically removed
# - Mutable: Can add or remove elements
# - Iterable: Can loop through the set

# 🔹 Creating Sets
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Duplicate values will be removed automatically
dup_set = {1, 2, 2, 3, 4}
print("Duplicate removed set:", dup_set)

# Empty set (must use set())
empty_set = set()
print("Empty set:", empty_set)

# 🔹 CRUD Operations on Set
# C - Create
numbers = {10, 20, 30}

# R - Read
for num in numbers:
    print("Element:", num)

# U - Update (Add elements)
numbers.add(40)
numbers.update([50, 60])
print("Updated set:", numbers)

# D - Delete
numbers.remove(30)         # Removes 30
numbers.discard(100)       # Safe remove, no error if not found
numbers.pop()              # Removes arbitrary item
print("After deletion:", numbers)

# 🔹 Set Functions
s = {1, 2, 3}
t = {3, 4, 5}

print("Union:", s.union(t))                  # {1, 2, 3, 4, 5}
print("Intersection:", s.intersection(t))    # {3}
print("Difference:", s.difference(t))        # {1, 2}
print("Symmetric Difference:", s.symmetric_difference(t))  # {1, 2, 4, 5}

# 🔹 Other Useful Methods
print("Length:", len(s))         # Count of elements
print("Contains 2:", 2 in s)     # Membership test

# Copying a set
s_copy = s.copy()
print("Copied set:", s_copy)

# Clearing all elements
s.clear()
print("Cleared set:", s)

# 🔹 When to Use Sets?
# - To eliminate duplicate entries
# - To perform fast membership checks
# - To do set operations like union, intersection

# 🔹 Final Tip:
# Sets cannot contain mutable elements like lists or other sets.
# Tuples can be added if they contain only immutable types.
example_set = {(1, 2), (3, 4)}
print("Set with tuples:", example_set)
