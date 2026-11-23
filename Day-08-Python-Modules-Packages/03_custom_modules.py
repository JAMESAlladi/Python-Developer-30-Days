# Day 08 - Creating Custom Modules

# Creating reusable functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Using the functions
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

# Testing division by zero
print("Division by zero:", divide(10, 0))


# Creating a reusable greeting function

def greet(name):
    return f"Hello, {name}! Welcome to Python modules."


print(greet("James"))
