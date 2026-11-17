# Day 03 - List and Tuple Operations

# 1. List concatenation
list1 = [10, 20, 30]
list2 = [40, 50, 60]

combined = list1 + list2
print("Combined List:", combined)

# 2. List repetition
repeated = list1 * 2
print("Repeated List:", repeated)

# 3. List slicing
numbers = [10, 20, 30, 40, 50, 60]

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Middle elements:", numbers[2:5])

# 4. Finding maximum and minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 5. Sum of list elements
print("Total:", sum(numbers))

# 6. Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2
print("Combined Tuple:", combined_tuple)

# 7. Tuple repetition
print("Repeated Tuple:", tuple1 * 2)

# 8. Tuple slicing
print("Tuple elements:", combined_tuple[1:4])

# 9. Converting list into tuple
my_tuple = tuple(numbers)
print("List converted to tuple:", my_tuple)

# 10. Converting tuple into list
my_list = list(tuple1)
print("Tuple converted to list:", my_list)
