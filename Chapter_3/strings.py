# 1️⃣ String Declaration
a = "Abhishek"   # Double quotes
b = 'Mittal'     # Single quotes
c = '''This is helpful in
multi-line string. You can write
text on multiple lines using triple quotes.'''

print("String a:", a)
print("String b:", b)
print("String c:", c)

# 2️⃣ Strings are Immutable
# You cannot change individual characters in a string
# a[0] = "M"  # ❌ This will cause an error

# But you can make a new string
new_a = "M" + a[1:]
print("Modified string a:", new_a)  # Mbhishek

# 3️⃣ Length of a String
lengthOfA = len(a)
print("Length of a:", lengthOfA)  # 8

# 4️⃣ String Slicing
# Syntax: string[start:end] --> includes start, excludes end
nameShort = a[0:4]
print("a[0:4]:", nameShort)  # Abhi
print("a[:4]:", a[:4])       # Abhi
print("a[4:]:", a[4:])       # shek

# 5️⃣ Negative Indexing
# Negative indexes start from the end (-1 = last char)
like = a[-7:-1]  # from index -7 to -2
print("a[-7:-1]:", like)  # bhishe

# 6️⃣ Useful String Methods
# Concatenation
fullName = a + " " + b
print("Full Name:", fullName)

# Changing case
print("Uppercase:", a.upper())  # ABHISHEK
print("Lowercase:", b.lower())  # mittal
print("Capitalize:", b.capitalize())  # Mittal

# Checking start and end
print("Starts with 'Ab':", a.startswith("Ab"))  # True
print("Ends with 'al':", b.endswith("al"))      # True

# Replace characters
print("Replace 'A' with 'O':", a.replace("A", "O"))  # Obhishek

# Split a sentence into words
sentence = "Hello Python Learners"
words = sentence.split()
print("Split words:", words)  # ['Hello', 'Python', 'Learners']

# Join list back into string
joined = "-".join(words)
print("Joined with hyphen:", joined)  # Hello-Python-Learners

# Remove leading/trailing spaces
spaces = "  Hello  "
print("Trimmed spaces:", spaces.strip())  # Hello

# 7️⃣ Extra String Functions for Practice
text = "Python is Fun"

print("Find 'is':", text.find("is"))         # 7
print("Count 'n':", text.count("n"))         # 2
print("Is alphabetic:", text.isalpha())      # False (space included)
print("Is alphanumeric:", text.replace(" ", "").isalnum())  # True
print("Is lowercase:", text.islower())       # False
print("Is uppercase:", text.isupper())       # False
print("Swap case:", text.swapcase())         # pYTHON IS fUN
print("Center the text:", text.center(30, "*"))  # ***Python is Fun***********

# 8️⃣ Multiline Practice String
multi = """Python is powerful.
It is easy to learn.
It is widely used."""

print("Multi-line string:\n", multi)