class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):               # Dog inherits from Animal
    def speak(self):             # method overriding
        print(f"{self.name} says Woof!")

d = Dog("Tommy")
d.speak()                        # Tommy says Woof!
