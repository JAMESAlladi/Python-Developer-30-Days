# Day 09 - File Handling and Exception Handling Challenges

# Challenge 1: Write data into a file

with open("notes.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("File handling is important.")

print("Challenge 1: File created successfully!")


# Challenge 2: Read data from a file

with open("notes.txt", "r") as file:
    content = file.read()

print("\nChallenge 2: File content:")
print(content)


# Challenge 3: Count the number of lines

with open("notes.txt", "r") as file:
    lines = file.readlines()

print("Challenge 3: Total lines:", len(lines))


# Challenge 4: Handle division errors

def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero"


print("\nChallenge 4:")
print("Result:", safe_divide(20, 5))
print("Result:", safe_divide(20, 0))


# Challenge 5: Handle invalid number input

def convert_to_integer(value):
    try:
        return int(value)

    except ValueError:
        return "Invalid input! Enter a number."


print("\nChallenge 5:")
print(convert_to_integer("100"))
print(convert_to_integer("Python"))
