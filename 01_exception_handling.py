# Day 7 - Exception Handling

try:
    a = 10
    b = 0

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

print("Program completed successfully")
