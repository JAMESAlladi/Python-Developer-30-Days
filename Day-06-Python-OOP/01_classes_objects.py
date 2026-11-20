# Day 06 - Python Classes and Objects

# 1. Creating a class

class Student:
    def display(self):
        print("Welcome to Python OOP!")


# 2. Creating an object

student1 = Student()

student1.display()


# 3. Class with attributes

class Employee:
    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee Role:", self.role)


# 4. Creating objects with attributes

employee1 = Employee()
employee1.name = "James"
employee1.role = "Python Developer"

employee2 = Employee()
employee2.name = "John"
employee2.role = "Data Analyst"

employee1.show_details()
employee2.show_details()


# 5. Class with multiple methods

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"

        return a / b


# 6. Creating calculator object

calc = Calculator()

print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))
