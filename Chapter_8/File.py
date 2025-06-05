# ✅ Opening a File
# Modes: 'r' = read, 'w' = write, 'a' = append, 'b' = binary, 'x' = create
file = open("example.txt", "w")  # Opens file for writing (creates if not exists)

# ✅ Writing to a File
file.write("Hello, this is a line in the file.\n")
file.write("This is another line.\n")
file.close()  # Always close the file after writing

# ✅ Reading a File
file = open("example.txt", "r")
content = file.read()  # Reads entire content
print("\nFile content:\n", content)
file.close()

# ✅ Reading line by line
file = open("example.txt", "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())  # .strip() removes \n
file.close()

# ✅ Appending to a File
file = open("example.txt", "a")
file.write("Appended line.\n")
file.close()

# ✅ Using 'with' Statement (Recommended)
# Automatically closes the file even if an error occurs
with open("example.txt", "r") as file:
    print("\nReading using with:")
    print(file.read())

# ✅ File Methods
# file.read(n) - reads first n characters
# file.readline() - reads one line
# file.readlines() - returns list of all lines

# ✅ Check if file exists (before reading or deleting)
import os
if os.path.exists("example.txt"):
    print("\nFile exists!")
else:
    print("File does not exist!")

# ✅ Deleting a file
# os.remove("example.txt")  # Uncomment to delete the file

# ✅ Creating a new file only if it doesn't exist
try:
    file = open("newfile.txt", "x")  # Fails if file exists
    file.write("This is a new file.")
    file.close()
except FileExistsError:
    print("newfile.txt already exists.")

# ✅ Binary mode (e.g., reading images or videos)
# with open("image.jpg", "rb") as img_file:
#     data = img_file.read()

# ✅ Summary:
# - Use open(filename, mode) and close() or 'with'
# - Modes: 'r', 'w', 'a', 'x', with 'b' for binary
# - Use os module to check or delete files
# - File I/O is essential for data storage and retrieval