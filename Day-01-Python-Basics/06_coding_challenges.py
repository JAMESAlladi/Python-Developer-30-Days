
# Day 01 - Python Coding Challenges

# Problem 1: Reverse a String
def reverse_string(text):
    return text[::-1]


print(reverse_string("Python"))


# Problem 2: Check Palindrome
def is_palindrome(text):
    return text == text[::-1]


print(is_palindrome("madam"))


# Problem 3: Find Largest Number
def find_largest(numbers):
    return max(numbers)


print(find_largest([10, 25, 5, 40, 15]))


# Problem 4: Count Vowels
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


print(count_vowels("Python Developer"))


# Problem 5: Remove Duplicates
def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
