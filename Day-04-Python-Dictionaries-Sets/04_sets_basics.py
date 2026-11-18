# Day 04 - Python Sets Basics

# 1. Creating a set
numbers = {10, 20, 30, 40, 50}
print("Numbers:", numbers)

# 2. Removing duplicate elements
values = {10, 20, 10, 30, 20, 40}
print("Unique values:", values)

# 3. Adding an element
numbers.add(60)
print("After adding:", numbers)

# 4. Adding multiple elements
numbers.update([70, 80, 90])
print("After update:", numbers)

# 5. Removing an element
numbers.remove(30)
print("After remove:", numbers)

# 6. Discarding an element
numbers.discard(100)
print("After discard:", numbers)

# 7. Union of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))

# 8. Intersection of sets
print("Intersection:", set1.intersection(set2))

# 9. Difference of sets
print("Difference:", set1.difference(set2))

# 10. Symmetric difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 11. Checking membership
if 20 in numbers:
    print("20 exists in the set")

# 12. Set length
print("Total elements:", len(numbers))
