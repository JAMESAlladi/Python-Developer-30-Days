# Day 09 - Python Exception Handling

# 1. Handling division by zero

try:
    result = 10 / 0
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# 2. Handling invalid input

try:
    number = int("hello")
    print("Number:", number)

except ValueError:
    print("Error: Invalid number")


# 3. Using multiple except blocks

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid integer")

except ZeroDivisionError:
    print("Error: Number cannot be zero")


# 4. Using else

try:
    number = 20 / 5

except ZeroDivisionError:
    print("Division error")

else:
    print("Successful result:", number)


# 5. Using finally

try:
    print("Executing try block")

except Exception:
    print("An error occurred")

finally:
    print("Finally block always executes")
