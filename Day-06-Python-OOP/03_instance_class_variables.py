class Student:
    school = "VIT-AP"            # class variable

    def __init__(self, name):
        self.name = name         # instance variable

s1 = Student("James")
s2 = Student("Asha")
print(s1.school, s2.school)      # both show VIT-AP
