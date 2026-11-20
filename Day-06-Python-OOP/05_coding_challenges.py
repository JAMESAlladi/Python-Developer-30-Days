# ---------------------------------------------------------
# Challenge 1: Library Book
# ---------------------------------------------------------
class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} borrowed")
        else:
            print("Already borrowed!")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.title} returned")
        else:
            print(f"{self.title} was not borrowed")


print("--- Challenge 1: Library Book ---")
book = Book("Python Basics", "Guido")
book.borrow()
book.borrow()
book.return_book()


# ---------------------------------------------------------
# Challenge 2: Bank Account with a minimum balance
# ---------------------------------------------------------
class BankAccount:
    min_balance = 500  # class variable shared by all accounts

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < BankAccount.min_balance:
            print(f"Insufficient balance (minimum {BankAccount.min_balance} required)")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account: {self.owner}, Balance: {self.balance}"


print("\n--- Challenge 2: Bank Account ---")
acc = BankAccount("James", 1000)
acc.deposit(500)
acc.withdraw(1200)   # would leave 300 -> blocked
acc.withdraw(700)    # leaves 800 -> allowed
print(acc)


# ---------------------------------------------------------
# Challenge 3: Student Grade Calculator
# ---------------------------------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        return "F"


print("\n--- Challenge 3: Grade Calculator ---")
students = [
    Student("Asha", [85, 90, 90]),
    Student("Ravi", [60, 55, 70]),
    Student("Meena", [95, 92, 98]),
]
for s in students:
    print(f"{s.name}: average {s.average():.1f}, grade {s.grade()}")


# ---------------------------------------------------------
# Challenge 4: Inheritance (Employee system)
# ---------------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee: {self.name}, {self.salary}")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show(self):
        print(f"Developer: {self.name}, {self.salary}, {self.language}")


class Tester(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def show(self):
        print(f"Tester: {self.name}, {self.salary}, {self.tool}")


print("\n--- Challenge 4: Employee System ---")
team = [
    Developer("James", 60000, "Python"),
    Tester("Ravi", 40000, "Selenium"),
    Employee("Asha", 50000),
]
for member in team:
    member.show()   # polymorphism: each class has its own show()


# ---------------------------------------------------------
# Challenge 5: Object counter and inventory
# ---------------------------------------------------------
class Product:
    total_products = 0  # class variable

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.total_products += 1

    def total_value(self):
        return self.price * self.quantity


print("\n--- Challenge 5: Inventory ---")
products = [
    Product("Laptop", 50000, 2),
    Product("Mouse", 500, 10),
    Product("Keyboard", 1500, 5),
]
for p in products:
    print(f"{p.name}: total value {p.total_value()}")
print(f"Total products: {Product.total_products}")
