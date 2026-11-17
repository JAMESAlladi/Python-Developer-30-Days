# Day 03 - Python Lists Basics

# 1. Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Fruits:", fruits)

# 2. Accessing list elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Updating list elements
fruits[1] = "Grapes"
print("Updated fruits:", fruits)

# 4. Finding the length of a list
print("Total fruits:", len(fruits))

# 5. Checking if an element exists
if "Mango" in fruits:
    print("Mango is available")

# 6. Looping through a list
for fruit in fruits:
    print(fruit)
