# Day 05 - Python Function Coding Challenges


# Challenge 1: Find the factorial of a number

def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

print("Challenge 1 - Factorial:", factorial(5))


# Challenge 2: Check whether a number is prime

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

print("Challenge 2 - Prime:", is_prime(17))


# Challenge 3: Find Fibonacci series

def fibonacci(count):
    series = []
    a, b = 0, 1

    for _ in range(count):
        series.append(a)
        a, b = b, a + b

    return series

print("Challenge 3 - Fibonacci:", fibonacci(10))


# Challenge 4: Check whether a string is palindrome

def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]

print("Challenge 4 - Palindrome:", is_palindrome("Madam"))


# Challenge 5: Calculate the average of a list

def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

marks = [85, 90, 78, 92, 88]

print("Challenge 5 - Average:", calculate_average(marks))
