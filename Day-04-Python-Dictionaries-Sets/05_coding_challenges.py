# Day 04 - Python Dictionary and Set Coding Challenges


# Challenge 1: Count the frequency of each element

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print("Challenge 1 - Frequency:", frequency)


# Challenge 2: Find duplicate elements

values = [10, 20, 30, 20, 40, 10, 50]

duplicates = set()
seen = set()

for value in values:
    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)

print("Challenge 2 - Duplicates:", duplicates)


# Challenge 3: Merge two dictionaries

dict1 = {"name": "James", "age": 24}
dict2 = {"course": "Python", "city": "Hyderabad"}

merged = {**dict1, **dict2}

print("Challenge 3 - Merged Dictionary:", merged)


# Challenge 4: Find common elements in two lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = set(list1).intersection(set(list2))

print("Challenge 4 - Common Elements:", common)


# Challenge 5: Find unique elements from two lists

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

unique = set(list1).symmetric_difference(set(list2))

print("Challenge 5 - Unique Elements:", unique)
