# Challenge 1: Reverse a string

text = "Python"

reversed_text = text[::-1]

print("Original String:", text)
print("Reversed String:", reversed_text)


# Challenge 2: Palindrome Checker

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Challenge 3: Count Vowels

text = "Python Developer"

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Total vowels:", count)



# Challenge 4: Character Frequency

text = "banana"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(char, ":", count)




# Challenge 5: Remove Duplicate Characters

text = "programming"

result = ""

for char in text:
    if char not in result:
        result += char

print("Original:", text)
print("Without duplicates:", result)


