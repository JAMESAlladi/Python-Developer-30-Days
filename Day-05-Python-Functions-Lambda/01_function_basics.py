# Day 05 - Python Function Basics

# 1. Creating a simple function

def greet():
    print("Hello, Welcome to Python!")

greet()


# 2. Function with parameters

def greet_user(name):
    print("Hello", name)

greet_user("James")


# 3. Function with multiple parameters

def add_numbers(a, b):
    result = a + b
    print("Addition:", result)

add_numbers(10, 20)


# 4. Function with return value

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)


# 5. Function to calculate square

def square(number):
    return number ** 2

print("Square:", square(6))


# 6. Function with default arguments

def introduce(name, country="India"):
    print(name, "is from", country)

introduce("James")
introduce("John", "France")


# 7. Function to check even or odd

def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number check:", check_number(10))


# 8. Function to find the largest number

def find_largest(a, b, c):
    return max(a, b, c)

print("Largest number:", find_largest(10, 25, 15))
