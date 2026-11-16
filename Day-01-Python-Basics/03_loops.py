
# Day 01 - Python Loops

# 1. For Loop
print("For Loop Example")

for i in range(1, 11):
    print(i)


# 2. Multiplication Table
number = 5

print("\nMultiplication Table")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# 3. While Loop
print("\nWhile Loop Example")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# 4. Sum of First 10 Numbers
total = 0

for i in range(1, 11):
    total += i

print("\nSum:", total)
