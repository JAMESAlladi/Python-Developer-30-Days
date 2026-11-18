# Day 04 - Python Nested Dictionaries

# 1. Creating a nested dictionary

students = {
    "student1": {
        "name": "James",
        "age": 24,
        "course": "Artificial Intelligence"
    },
    "student2": {
        "name": "John",
        "age": 23,
        "course": "Data Science"
    },
    "student3": {
        "name": "David",
        "age": 25,
        "course": "Computer Science"
    }
}

# 2. Displaying the complete dictionary
print("All Students:", students)

# 3. Accessing nested values
print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Course:", students["student2"]["course"])

# 4. Updating nested values
students["student1"]["age"] = 25
print("Updated Student 1:", students["student1"])

# 5. Adding a new student
students["student4"] = {
    "name": "Sarah",
    "age": 22,
    "course": "Machine Learning"
}

print("After adding student:", students)

# 6. Looping through nested dictionaries
for student_id, details in students.items():
    print("\nStudent ID:", student_id)

    for key, value in details.items():
        print(key, ":", value)

# 7. Removing a student
students.pop("student3")
print("\nAfter removing student 3:", students)

# 8. Counting students
print("Total students:", len(students))
