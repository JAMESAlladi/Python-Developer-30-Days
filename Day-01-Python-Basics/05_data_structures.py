
# Day 01 - Python Data Structures

# 1. List
skills = ["Python", "SQL", "FastAPI", "Django"]

skills.append("Flask")

print("List:", skills)
print("First Skill:", skills[0])


# 2. Tuple
coordinates = (10, 20, 30)

print("\nTuple:", coordinates)
print("First Coordinate:", coordinates[0])


# 3. Set
languages = {"Python", "Java", "Python", "C++"}

print("\nSet:", languages)
print("Unique Languages:", len(languages))


# 4. Dictionary
developer = {
    "name": "James",
    "role": "Python Developer",
    "skills": ["Python", "SQL", "FastAPI"]
}

print("\nDictionary:", developer)
print("Developer Name:", developer["name"])


# 5. Dictionary Iteration
for key, value in developer.items():
    print(key, ":", value)
