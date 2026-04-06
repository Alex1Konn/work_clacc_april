"""
Методы классы
self - ссылается на экземпляр

класс метод это декоратор говорит что эт относится к классу
isinstance() - проверяет какой экщемпляр класса относиться к классу. Вывод True или False.
Внутри метода можно создать еще методы

class MyClass:
    name = "QWERTY"

    @classmethod
    def set_attr(cls, new_name):
        cls.name = new_name

    @classmethod
    def get_attr(cls):
        return cls.name

MyClass.get_attr()
MyClass.set_attr("Василий")

print(MyClass.name)

class Point:

    @classmethod
    def create(cls):
        return cls()

point = Point.create()
print(isinstance(point, Point))

Что такое cls - ссылка на класс. *параметр ссылка на класс

class Calculator:
    @classmethod
    def multiplication(cls, x, y):
        cls.x = x
        cls.y = y
        print(cls.x * cls.y)

Calculator.multiplication(5, 20)

class Counter:
    count = 0

    @classmethod
    def add_count(cls, add=1):
        cls.count += add
        return cls.count

    @classmethod
    def set_zero(cls):
        cls.count = 0
        return cls.count

print(Counter.add_count())
print(Counter.set_zero())
print(Counter.add_count(110))

class MyClass:
    @staticmethod
    def sum_static(a, b):
        return a + b

obj = MyClass()
print(MyClass.sum_static(1, 2))

class MyClass:
    @staticmethod
    def hello():
        return "hello"

print(type(MyClass.hello))

class Driver:
    @staticmethod
    def calculate_fuel_costs(distance, fuel, price):
        result = distance * (fuel/100) * price
        print(round(result, 2))

vasya = Driver()
vasya.calculate_fuel_costs(100,7, 50)

#Наследование. Родительский класс и дочерний класс

class Transport():
    pass

class Car(Transport):
    pass

class Transport():
    name = 'car'

    def get_name(self):
        return self.name

class Car(Transport):
    pass

toyota = Car()

class Car(Transport):
    pass
print(toyota.name, toyota.get_name())

class Transport:
    name_transport = 'класс Transport'
    def get_transport(self):
        return 'Метод Transport'

class Car(Transport):
    name_car = 'атрибут Car'

    def get_car(self):
        return "Метод Car"

car = Car() #может вызывать атрибуты и экземпляры и родительского и дочернего класс
print(car.name_car)
print(car.get_car())
print(car.name_transport)
print(car.get_transport())

transport = Transport() #не может вызвать атрибуты дочернего класс
print(transport.name_transport)
print(transport.get_transport())

Наследование создано, чтобы меньше писать код т.е. устраняет дублирование кода


class Transport:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

class Car(Transport):
    pass

class Airplane(Transport):
    pass

class Train(Transport):
    pass

toyota = Car('Легковой автомобиль', 100)
tu_154 = Airplane("амолет", 1000)
poezd = Train('поезд', 300)

print(toyota.__dict__)
print(tu_154.__dict__)
print(poezd.__dict__)

class Homer:
   def __init__(self, name):
        self.name = name

class Daughter(Homer):
   pass

daughter1 = Daughter
daughter1.name = 'Liza'
print(daughter1.name)


#области видения наследования от локального к родителю

class Transport:
    name = 'toyota'

class Avto(Transport):
    pass

rav4 = Avto()
print(rav4.name)

"""

# Переопредение

class Transport:
    name1 = 'toyota'
    name2 = 'subaru'
    name3 = 'opel'

class Avto(Transport):
    name2 = 'lada'

rav4 = Avto()
rav4.name3 = 'Vaz'

# print(rav4.name1)
# print(rav4.name2)
# print(rav4.name3)

# print(Avto.name1)
# print(Avto.name2)
# print(Avto.name3)

# print(Transport.name1)
# print(Transport.name2)
# print(Transport.name3)

class Cat:
    def say_cats(self):
        print('Hello Cats')

    def say_dogs(self):
        print('Hello Dogs')

class Dog(Cat):
    def say_dogs(self):
        print('Ваф! Ваф!')

# cat = Cat()
# cat.say_dogs()
# cat.say_cats()

# dog = Dog()
# dog.say_dogs()
# dog.say_cats()
