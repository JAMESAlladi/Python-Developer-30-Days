# Day 03 - Python Tuples Basics

# 1. Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange")
print("Fruits:", fruits)

# 2. Accessing tuple elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Tuple length
print("Total fruits:", len(fruits))

# 4. Checking an element
if "Mango" in fruits:
    print("Mango is available")

# 5. Looping through a tuple
for fruit in fruits:
    print(fruit)

# 6. Tuple with different data types
student = ("James", 24, "Artificial Intelligence")
print("Student:", student)

# 7. Tuple methods
numbers = (10, 20, 10, 30, 10)
print("Count of 10:", numbers.count(10))
print("Index of 20:", numbers.index(20))

# 8. Tuple unpacking
name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

# 9. Single-element tuple
single = ("Python",)
print("Single element tuple:", single)
