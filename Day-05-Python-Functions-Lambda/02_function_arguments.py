# Day 05 - Python Function Arguments

# 1. Positional Arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("James", 24)


# 2. Keyword Arguments

def employee(name, salary):
    print("Employee:", name)
    print("Salary:", salary)

employee(salary=50000, name="John")


# 3. Default Arguments

def welcome(name, message="Welcome to Python"):
    print(message, name)

welcome("James")
welcome("David", "Good Morning")


# 4. Multiple Arguments

def add(a, b, c):
    return a + b + c

print("Addition:", add(10, 20, 30))


# 5. Return Multiple Values

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication

result = calculate(20, 10)

print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])


# 6. Function with Conditional Logic

def check_age(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

print("Age Status:", check_age(24))


# 7. Passing a List to a Function

def calculate_total(numbers):
    return sum(numbers)

marks = [85, 90, 78, 92, 88]

print("Total Marks:", calculate_total(marks))
print("Average Marks:", calculate_total(marks) / len(marks))
