# Day 08 - Built-in Python Modules

# 1. Math module
import math

numbers = [10, 20, 30, 40, 50]

print("Square root:", math.sqrt(144))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Greatest common divisor:", math.gcd(12, 18))

# 2. Random module
import random

print("Random number:", random.randint(1, 100))
print("Random choice:", random.choice(numbers))

# 3. Datetime module
import datetime

today = datetime.date.today()
print("Today's date:", today)

current_time = datetime.datetime.now()
print("Current date and time:", current_time)

# 4. Statistics module
import statistics

values = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(values))
print("Median:", statistics.median(values))

# 5. OS module
import os

print("Current directory:", os.getcwd())
print("Python file name:", os.path.basename(__file__))
