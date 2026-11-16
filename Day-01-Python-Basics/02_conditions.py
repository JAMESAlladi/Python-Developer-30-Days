
# Day 01 - Conditional Statements

# Check whether a number is positive,
# negative, or zero.

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")

elif number < 0:
    print("The number is negative")

else:
    print("The number is zero")


# Check voting eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
