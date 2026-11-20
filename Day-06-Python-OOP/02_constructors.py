class Student:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age

s1 = Student("James", 24)     # __init__ runs automatically
print(s1.name, s1.age)
