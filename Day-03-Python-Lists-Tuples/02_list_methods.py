# Day 03 - Python List Methods

numbers = [10, 20, 30, 40]

# 1. append() - Add an element
numbers.append(50)
print("Append:", numbers)

# 2. insert() - Add at a specific position
numbers.insert(1, 15)
print("Insert:", numbers)

# 3. extend() - Add multiple elements
numbers.extend([60, 70])
print("Extend:", numbers)

# 4. remove() - Remove a specific element
numbers.remove(30)
print("Remove:", numbers)

# 5. pop() - Remove an element by index
numbers.pop(0)
print("Pop:", numbers)

# 6. sort() - Sort the list
numbers.sort()
print("Sort:", numbers)

# 7. reverse() - Reverse the list
numbers.reverse()
print("Reverse:", numbers)

# 8. count() - Count occurrences
values = [10, 20, 10, 30, 10]
print("Count:", values.count(10))

# 9. index() - Find an element position
print("Index:", values.index(20))

# 10. copy() - Copy a list
new_list = numbers.copy()
print("Copied List:", new_list)

# 11. clear() - Remove all elements
new_list.clear()
print("Cleared List:", new_list)
