# 🔹 What is OOP?
# Object-Oriented Programming is a paradigm based on the concept of "objects"
# which contain data (attributes) and functions (methods).

# ✅ Defining a Class
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name            # Attributes
        self.age = age

    def greet(self):                # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# ✅ Creating Objects (Instances)
p1 = Person("Abhishek", 21)
p1.greet()

# ✅ Class vs Instance Variables
class Student:
    college = "XYZ University"  # Class variable (shared)

    def __init__(self, name):
        self.name = name        # Instance variable

s1 = Student("Abhi")
s2 = Student("Mittu")
print(s1.name, s1.college)
print(s2.name, s2.college)

# ✅ Inheritance (One class inherits from another)
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Method Overriding
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks

# ✅ Multiple Inheritance
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

c = Child()
c.skills()

# ✅ Encapsulation (Hiding internal data)
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# ✅ Polymorphism (same method name, different behavior)
class Bird:
    def sound(self):
        print("Birds chirp")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

class Crow(Bird):
    def sound(self):
        print("Crow caws")

for bird in [Parrot(), Crow()]:
    bird.sound()

# ✅ Special Methods (Dunder Methods)
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python Basics")
print(b)  # Calls __str__ method

# ✅ Class Methods and Static Methods
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

    @staticmethod
    def greet():
        print("Hello from static method")

obj1 = MyClass()
obj2 = MyClass()
MyClass.show_count()
MyClass.greet()

# ✅ Summary of Key Concepts:
# - Class & Object
# - Instance vs Class Variables
# - Constructor (__init__)
# - Inheritance & Method Overriding
# - Multiple Inheritance
# - Encapsulation (private vars)
# - Polymorphism
# - Dunder Methods (__str__, etc.)
# - @classmethod & @staticmethod