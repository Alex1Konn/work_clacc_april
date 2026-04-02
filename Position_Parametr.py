
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
class Distance:
    distanse1 = 0
    distanse2 = 0
    def __init__(self, distanse1, distanse2):
    def count_distance(self, point1, point2):
        if point1 == point2:
            print(0)
        elif

