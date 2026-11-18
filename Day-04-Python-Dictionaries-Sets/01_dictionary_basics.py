# Day 04 - Python Dictionary Basics

# 1. Creating a dictionary
student = {
    "name": "James",
    "age": 24,
    "course": "Artificial Intelligence",
    "city": "Hyderabad"
}

print("Student:", student)

# 2. Accessing dictionary values
print("Name:", student["name"])
print("Age:", student["age"])

# 3. Using get()
print("Course:", student.get("course"))

# 4. Adding a new key-value pair
student["university"] = "EPITA"
print("After adding:", student)

# 5. Updating a value
student["age"] = 25
print("After updating:", student)

# 6. Checking if a key exists
if "name" in student:
    print("Name key exists")

# 7. Looping through a dictionary
for key, value in student.items():
    print(key, ":", value)

# 8. Dictionary length
print("Total items:", len(student))
