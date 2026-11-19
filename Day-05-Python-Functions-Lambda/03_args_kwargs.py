# Day 05 - Python *args and **kwargs


# 1. Using *args
# Accepts multiple positional arguments

def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total

print("Addition:", add_numbers(10, 20, 30))
print("Addition:", add_numbers(5, 10, 15, 20))


# 2. Finding the maximum using *args

def find_maximum(*numbers):
    return max(numbers)

print("Maximum:", find_maximum(10, 50, 30, 90, 20))


# 3. Using **kwargs
# Accepts multiple keyword arguments

def display_student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_student(
    name="James",
    age=24,
    course="Artificial Intelligence"
)


# 4. Combining *args and **kwargs

def employee_details(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

employee_details(
    "James",
    "Developer",
    age=24,
    country="India"
)


# 5. Calculating average using *args

def calculate_average(*marks):
    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)

print("Average:", calculate_average(80, 90, 85, 95))


# 6. Using **kwargs to create a dictionary

def create_profile(**details):
    return details

profile = create_profile(
    name="James",
    role="Python Developer",
    experience="Beginner"
)

print("Profile:", profile)
