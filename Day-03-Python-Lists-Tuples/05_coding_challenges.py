# Day 03 - Python List and Tuple Coding Challenges

# Challenge 1: Find the largest number in a list

numbers = [12, 45, 7, 89, 23]

largest = max(numbers)

print("Challenge 1 - Largest number:", largest)


# Challenge 2: Find the second largest number

numbers = [10, 20, 40, 30, 50]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("Challenge 2 - Second largest:", second_largest)


# Challenge 3: Remove duplicate elements from a list

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(dict.fromkeys(numbers))

print("Challenge 3 - Without duplicates:", unique_numbers)


# Challenge 4: Find the common elements in two lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = list(set(list1) & set(list2))

print("Challenge 4 - Common elements:", sorted(common))


# Challenge 5: Convert a list into a tuple

fruits = ["Apple", "Banana", "Mango"]

fruits_tuple = tuple(fruits)

print("Challenge 5 - Converted tuple:", fruits_tuple)
