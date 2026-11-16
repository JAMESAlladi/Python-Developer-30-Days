
# Day 01 - Python Functions

# 1. Simple Function
def greet():
    print("Welcome to Python Development!")


greet()


# 2. Function with Parameters
def add(a, b):
    return a + b


result = add(10, 20)
print("Addition:", result)


# 3. Calculate Factorial
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print("Factorial:", factorial(5))


# 4. Check Even or Odd
def check_number(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


print("Number:", check_number(10))
