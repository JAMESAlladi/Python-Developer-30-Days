# Day 04 - Python Dictionary Methods

student = {
    "name": "James",
    "age": 24,
    "course": "Artificial Intelligence"
}

# 1. keys() - Get all keys
print("Keys:", student.keys())

# 2. values() - Get all values
print("Values:", student.values())

# 3. items() - Get key-value pairs
print("Items:", student.items())

# 4. get() - Access a value
print("Name:", student.get("name"))

# 5. update() - Update dictionary values
student.update({"age": 25})
print("Updated:", student)

# 6. pop() - Remove an item
student.pop("course")
print("After pop:", student)

# 7. setdefault() - Add a key if missing
student.setdefault("city", "Hyderabad")
print("After setdefault:", student)

# 8. copy() - Copy dictionary
new_student = student.copy()
print("Copied dictionary:", new_student)

# 9. popitem() - Remove the last inserted item
new_student.popitem()
print("After popitem:", new_student)

# 10. clear() - Remove all items
new_student.clear()
print("After clear:", new_student)
