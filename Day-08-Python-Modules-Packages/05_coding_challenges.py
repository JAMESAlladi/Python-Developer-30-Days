# Day 08 - Python Modules and Packages Coding Challenges

# Challenge 1: Calculate square root using math module

import math

number = 144

print("Challenge 1 - Square root:", math.sqrt(number))


# Challenge 2: Generate a random number

import random

random_number = random.randint(1, 100)

print("Challenge 2 - Random number:", random_number)


# Challenge 3: Calculate mean and median

import statistics

numbers = [10, 20, 30, 40, 50]

print("Challenge 3 - Mean:", statistics.mean(numbers))
print("Challenge 3 - Median:", statistics.median(numbers))


# Challenge 4: Calculate factorial

factorial_number = 5

result = math.factorial(factorial_number)

print("Challenge 4 - Factorial:", result)


# Challenge 5: Create reusable calculator functions

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


print("Challenge 5 - Addition:", add(20, 10))
print("Challenge 5 - Subtraction:", subtract(20, 10))
print("Challenge 5 - Multiplication:", multiply(20, 10))
print("Challenge 5 - Division:", divide(20, 10))
