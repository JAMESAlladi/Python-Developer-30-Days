# Day 09 - Reading and Writing Files

# 1. Writing multiple lines into a file
with open("students.txt", "w") as file:
    file.write("James\n")
    file.write("Alex\n")
    file.write("John\n")
    file.write("David\n")

print("Student names saved successfully!")

# 2. Reading the complete file
with open("students.txt", "r") as file:
    content = file.read()

print("\nAll Students:")
print(content)

# 3. Reading one line
with open("students.txt", "r") as file:
    first_line = file.readline()

print("First Student:", first_line.strip())

# 4. Reading all lines into a list
with open("students.txt", "r") as file:
    students = file.readlines()

print("Student List:", students)

# 5. Appending a new student
with open("students.txt", "a") as file:
    file.write("Michael\n")

print("New student added!")

# 6. Count the number of students
with open("students.txt", "r") as file:
    students = file.readlines()

print("Total Students:", len(students))
