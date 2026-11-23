# Day 08 - Python Packages Basics

# A package organizes multiple Python modules.

# 1. Importing a package module
import math

print("Square root:", math.sqrt(100))

# 2. Importing a specific function
from math import factorial

print("Factorial:", factorial(5))

# 3. Importing with an alias
import statistics as stats

numbers = [10, 20, 30, 40, 50]

print("Mean:", stats.mean(numbers))
print("Median:", stats.median(numbers))

# 4. Creating functions that could belong
# to separate modules inside a package

def calculate_area(length, width):
    return length * width


def calculate_perimeter(length, width):
    return 2 * (length + width)


print("Area:", calculate_area(10, 5))
print("Perimeter:", calculate_perimeter(10, 5))

# 5. Understanding __name__
print("Module name:", __name__)

if __name__ == "__main__":
    print("This file is running directly.")
