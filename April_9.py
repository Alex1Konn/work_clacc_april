"""
Наследование
Object это корневой класс. Родитель всех классов.
СОздан программистами, чтобы от него наследовались созданныее классы.
Это помогает принять нам встреонные методи init dict и т.д.

Полиформизм =пример с фигурами, метод вычеление площади для всех один, но формулы разыне
Это возможность использовать один тот же метод для экземпляров из разын классов.
ОДин и тот же метод это метод содинаковым именем.А так же для разных  объектов.

class Person:
    pass

Person.

class Animal:
    def speak(self):
        print("i am an animal")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()

class Tree:
    def (self):
        print("некто")

class Grandfather(Tree):
    def status(self):
        print("дед")

class Vasya(Tree):
    def status(self):
        print("отец")

class Masha(Tree):
    def status(self):
        print("дочь")
masha = Masha()
vasya = Vasya()

masha.status()
vasya.status()

Функция super() - когда нужно обратиться к объектам класс через временный объект (проуси объект)
super().метод()
super().атрибут
MRO - method resolution order (порядок разрешения методов)
super(Child, self).greet()
Множественное наследование понять разницу между множественным наследвоание и цепочкой методов
#
class Cat():
    def hello_cat(self):
        self.name = "Hello cat"

class Dog(Cat):
    def hello_dog(self):
        super().hello_cat()

test = Dog()
test.hello_cat()
print(test.name)

Обращение к атрибуту

class Cat:
    name = "Cat"

class Dog(Cat):
    def print_name(self):
        print(super().name)

test = Dog()
test.print_name()

# __init__ и super()
class Cat:
   def __init__(self):
       self.cat = 'котик'

class Test(Cat):
    def __init__(self):
        super().__init__()
        self.dog = 'песик'
        print(self.dog)

test = Test()
print(test.cat)
print(test.dog)

super() - позволяет обращаться к классу без испоьзования имени класса

class Minecraft:
    def hello_creper(self):
        self.name = "hello creper"
        print(self.name)

class Roblox(Minecraft):
    def hello_all(self):
        super().hello_creper()
        self.new_name = "hello Pozzy"
        print(self.new_name)


hello = Roblox()
minecraft = Minecraft()

minecraft.hello_creper()
hello.hello_all()

class Alfa:
    def sum_number(self, x, y):
        self.x = x
        self.y = y
        print(self.x + self.y)

class Beta(Alfa):
    def result(self, x, y, *args):
        super().sum_number(x, y)
        self.z = z
        #print(self.x + self.y + self.z)

test = Beta()
test.result(10, 20,50)

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Student(Person):
    def __init__(self, name, age, height, weight, class_number, hobby):
        super().__init__(name, age, height, weight)
        self.class_number = class_number
        self.hobby = hobby

class Worker(Person):
    def __init__(self, name, age, height, weight, work, experience):
        super().__init__(name, age, height, weight)
        self.work = work
        self.experience = experience

id1 = Student('Таня', 6, 100, 25, 1,"готовить",)
id2 = Worker('Tanya', 6, 100, 25, "водитель", 6)

print(id1.__dict__)
print(id2.__dict__)



class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()

#Множественное наследование ( от нескольких родительских классов)
class A:
    def method1(self):
        print("Method 1 from A")

class B:
    def method2(self):
        print("Method 2 from B")

class C(A, B):
    def method3(self):
        print("Method 3 from C")

child = C()
child.method1()
child.method2()
child.method3()
"""

class King:
    a = 4

class Queen():
    b = 6

class Prince(King, Queen):
    c = 10

count = Prince()
print(count.a + count.b + count.c)
