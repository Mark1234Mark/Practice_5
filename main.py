'''

Хіленко Марк ШІД-32
markhilenko@gmail.com

'''

# 1) Створіть клас Animal, додайте docstring, три атрибути, один з яких має значення за замовчуванням та два методи на свій розсуд.
# 1.1. (5б). Створіть два обʼєкти цього класу. На одному обʼєкті отримайте значення його атрибуту, а на іншому викличте один з його методів.

class Animal:

    def __init__(self, name, species, age=0):
        self.name = name
        self.species = species
        self.age = age

    def sound(self):
        print(f"{self.name} makes a sound.")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

dog = Animal("Buddy", "Dog")
print(dog.name)
print(dog.species)
dog.sound()

cat = Animal("Whiskers", "Cat", 2)
print(cat.name)
print(cat.age)
cat.birthday()


# 2)  Створіть клас, де атрибути мають різні рівні доступу. Спробуйте отримати їхні значення та опишіть результати.

class Example:
    def __init__(self):
        self.public = "Public attribute"
        self._protected = "Protected attribute"
        self.__private = "Private attribute"

example = Example()
print(example.public)
print(example._protected)
# print(example.__private)  # This will raise an AttributeError
print(example._Example__private)  # This is how to access private attribute


# 3) Як ви розумієте термін self? Для чого використовується метод __init __?

'''

self - це посилання на сам екземпляр класу. Використовується для доступу до атрибутів та методів класу. 
У Python ключове слово self використовується для представлення екземпляра класу. За його допомогою можна отримати доступ до атрибутів та методів класу в Python.

__init__ - це особливий метод у класах Python, відомий як конструктор. 
Цей метод викликається при створенні об'єкта з класу і дозволяє класу ініціалізувати атрибути класу.

'''

# 4) Створіть клас Фігура без атрибутів, з методом get_area для отримання площі фігури, що повертає 0 та __add __,
# який приймає self та other в якості аргументів, а повертає суму площин фігур self та other.

class Shape:
    def get_area(self):
        return 0

    def __add__(self, other):
        return self.get_area() + other.get_area()

# 5)  Створіть 2 дочірніх класи від Фігури: Трикутник та Коло, які мають атрибути, необхідні для розрахунку площин. Визначте метод get_area в кожному з них так, щоби вони розраховували площу в залежності від формули для кожного типу фігури.
# Створіть обʼєкт класу Трикутник та обʼєкт класу Коло. Виконайте операцію суми за допомогою оператора + між ними.

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

triangle = Triangle(4, 5)
circle = Circle(3)
print(triangle + circle)

# 6) Продемонструйте різницю між isinstance та issubclass

class A:
    pass

class B(A):
    pass

a = A()
b = B()

print(isinstance(a, A))  # True
print(isinstance(b, A))  # True
print(issubclass(B, A))  # True

# 7) Створіть клас BankAccount з приватними атрибутами balance та account_number. Реалізуйте методи поповнення та зняття коштів,
# забезпечивши належну інкапсуляцію. Підказка: використовуйте декоратори getter та setter.

class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# 8)  Створіть клас Library, який містить список об'єктів типу Book. Реалізуйте методи для додавання книги, видалення книги та відображення списку книг.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")


# 9) Створіть клас Person з атрибутами name та age. Створіть ще один клас Employee з такими атрибутами, як department та salary.
# Створіть клас Manager, який успадковує обидва класи Person та Employee.
# Продемонструйте використання множинної спадковості, створивши обʼєкт класу Manager та отримавши mro для цього класу.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, department, salary):
        self.department = department
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, age, department, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, department, salary)

manager = Manager(name="Any Name", age=25, department="IT", salary=50000)

print(f"Name: {manager.name}")
print(f"Age: {manager.age}")
print(f"Department: {manager.department}")
print(f"Salary: {manager.salary}")


print(f"MRO for Manager: {Manager.mro()}")
