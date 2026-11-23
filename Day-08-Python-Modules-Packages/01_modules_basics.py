# Day 08 - Python Modules Basics

# A module is a Python file containing reusable code.

# 1. Importing the math module
import math

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Pi value:", math.pi)

# 2. Importing the random module
import random

number = random.randint(1, 100)
print("Random number:", number)

# 3. Importing the datetime module
import datetime

today = datetime.date.today()
print("Today's date:", today)

# 4. Importing specific functions
from math import factorial

print("Factorial:", factorial(5))

# 5. Using an alias
import math as m

print("Square root using alias:", m.sqrt(64))
