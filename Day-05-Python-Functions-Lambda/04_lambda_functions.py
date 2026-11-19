# Day 05 - Python Lambda Functions

from functools import reduce

# 1. Normal function
def square(number):
    return number * number

print("Normal Function:", square(5))


# 2. Lambda function
square_lambda = lambda number: number * number

print("Lambda Function:", square_lambda(5))


# 3. Lambda with multiple arguments
addition = lambda a, b: a + b

print("Addition:", addition(10, 20))


# 4. Using map() - Square every number
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Squares:", squares)


# 5. Using filter() - Find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


# 6. Using reduce() - Calculate total
total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)


# 7. Lambda with strings
names = ["James", "John", "David", "Sarah"]

sorted_names = sorted(names, key=lambda name: len(name))

print("Sorted by Name Length:", sorted_names)


# 8. Find numbers greater than 10
values = [5, 12, 8, 20, 15, 3]

result = list(filter(lambda x: x > 10, values))

print("Numbers Greater Than 10:", result)


# 9. Convert temperatures
celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("Fahrenheit:", fahrenheit)


# 10. Multiply all numbers
product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)
