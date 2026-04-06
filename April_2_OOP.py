"""
class Person:
    name = "Василий"

id_1 = Person()

print(hasattr(Person, "name"))
print(hasattr(id_1, "name"))
print(hasattr(id_1, "age"))

class Pokemon:
    pass
pokemon_1 = Pokemon()
setattr(pokemon_1, "picachu", " ")
setattr(pokemon_1, "scuther", " ")
setattr(pokemon_1, "gyarados", " ")
setattr(pokemon_1, "gengar", " ")

print(hasattr(pokemon_1, "picachu"))
print(hasattr(pokemon_1, "lapras"))
print(hasattr(pokemon_1, "alakazam"))


class Person:
    pass
id_1 = Person()
setattr(id_1, "name", "Василий")
print(hasattr(id_1, "name"))

delattr(id_1, 'name')
print(hasattr(id_1, "name"))


from stringprep import in_table_d1


class Person:
    name = "Василий"

id_1 = Person()

if hasattr(id_1, "name"):
    delattr(id_1, "name")

print(hasattr(id_1, "name")) # ошибка т.к. нет наследования


class Calculator:
    def addition(self):
        print("складываем числа")

calc = Calculator()
calc.addition()
Calculator.addition(" ")
#обращение к классу возможно только при заполнении параметра пустая строка или self т.к. на это расчитан метод


#Методы выполняюдт какое-о действие. Имя метода это глагол описывающий действующий. Вывоз метода поход на вызов атрибута. толкь т

class Kitty:
    def say_hello(self):
        print("Hello, Kitty")

cat = Kitty()
cat.say_hello()

def add_numbers(x, y):
    return x + y

print(add_numbers(10, 3))

result =  add_numbers(10, 5)
print(result)


class Number:
    a = 10
    b = 5

first = Number()
print(first.a + first.b)


class Calculator:
    a = 10
    b = 4

   def addition(self):
       summa = self.a + self.b
       print(summa)

first = Calculator()
first.addition()

a = 10
b = 5

def addition():
    summa = a + b
    print(summa)

addition()

class Calculator:
    a = 10
    b = 4

    def addition(self):
        summa = self.a + self.b # или класс Calculator.a + Calculator.b
        print(summa)

first = Calculator()
first.addition()

#self всегда используется для работы с атрибутами и методамит для экземпляров

class Mult:
    def say_hello(self, name):
        print(f"Hello {name}!")

mult_1 = Mult()
mult_1.say_hello("Bart")
mult_1.say_hello("Lisa")
"""

class Person:
    def print_number_of_messages(self, message_counter):
        print(f"{message_counter} messages")

pers_1 = Person()
pers_1.print_number_of_messages(10)
pers_2 = Person()
pers_2.print_number_of_messages(15)


"""
from struct import calcsize

Позизионные параметры

self - не позицонный параметр
cal.addition(1, 2) - в скобках позиционные параметры


class Calculator:
    def addition(self, a, b):
        print(a + b)

cal = Calculator()
cal.addition(1, 2)


Параметры по умолчанию
если не укажем какой-т о параметр, то будет подятигиваться параметры по усмолячанию


class Calculator:
    def addition(self, a=0, b=0):
        print(a + b)

cal = Calculator()
cal.addition(1, 4)
cal.addition(4)
cal.addition(0)

#*args **kwargs
class Calculator:
    def addition(self, *args, **kwargs):
        print(sum(args))

cal = Calculator()
cal.addition(1, 4, 3, 9, 9)

class Calculator:
    def plus(self, a, b):
        print(a + b)

calc = Calculator()
calc.plus(10, 5)

class Person:
    def set_attr(self, name, age):
        self.name = name
        self.age = age

person_1 = Person()
person_1.set_attr('василий', 15)

print(person_1.name, person_1.age)


class Person:
    def set_attr(self, name, age):
        setattr(self, 'name', age)
        setattr(self, 'age', age)

person_1 = Person()
person_1.set_attr('Василий', 15)
print(person_1.name, person_1.age)


class NewJournal:
    def set_attr(self, mama, papa, deda, baba):
        self.mama = mama
        self.papa = papa
        self.deda = deda
        self.baba = baba

    def chek_money(self, count_money):
        count_money = self.papa + self.deda + self.baba + self.mama
        if count_money < 80:
            print(f'Денег не хватает')
        else:
            print("Ура! Денег хвататет!")

masha = NewJournal()
setattr(masha,'mama', 30)
setattr(masha,'papa', 40)
setattr(masha,'deda', 20)
setattr(masha,'baba', 10)

masha.chek_money(" ")

"""
class GPS:
    def __init__(self):
        self.distance1 = ("Москва", "Самара", 1860)
        self.distance2 = ("Самара", "Сызрань", 820)
        self.distance3 = ("Самара", "Тольятти", 350)

    def count_distance(self, point1, point2):
        if point1 == point2:
            print(0)
        else:
            for attr in [self.distance1, self.distance2, self.distance3]:
                if point1 in attr and point2 in attr:
                    print(attr[2])
                    break
            else:
                print("Извините, программа еще в разработке.")

nav = GPS()
nav.count_distance("Москва", "Самара")
nav.count_distance("Тольятти", "Тольятти")


