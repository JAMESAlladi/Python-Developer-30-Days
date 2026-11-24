# Day 09 - Custom Exceptions in Python

# 1. Creating a custom exception

class InvalidAgeError(Exception):
    pass


# 2. Function to validate age

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    return "Access granted"


# 3. Handling custom exception

try:
    age = 16
    result = check_age(age)
    print(result)

except InvalidAgeError as error:
    print("Custom Error:", error)


# 4. Creating another custom exception

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient account balance"
        )

    return balance - amount


# 5. Testing withdrawal

try:
    balance = 5000
    amount = 7000

    remaining = withdraw(balance, amount)

    print("Remaining balance:", remaining)

except InsufficientBalanceError as error:
    print("Transaction Error:", error)


# 6. Handling multiple exceptions

class NegativeNumberError(Exception):
    pass


def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError(
            "Number cannot be negative"
        )

    return number ** 0.5


try:
    print("Square root:", calculate_square_root(-25))

except NegativeNumberError as error:
    print("Calculation Error:", error)
