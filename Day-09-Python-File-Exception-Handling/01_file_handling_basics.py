# Day 09 - Python File Handling Basics

# 1. Writing data into a file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("Learning File Handling.\n")
    file.write("Day 09 Python Developer Challenge.")

print("File created successfully!")

# 2. Reading data from a file
with open("sample.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# 3. Appending new content
with open("sample.txt", "a") as file:
    file.write("\nPracticing Python every day!")

print("\nNew content added successfully!")

# 4. Reading the updated file
with open("sample.txt", "r") as file:
    updated_content = file.read()

print("\nUpdated File Content:")
print(updated_content)

# 5. Reading file line by line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
