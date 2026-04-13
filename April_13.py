"""
Порядок множественного наследования

class C(A, B) или class С(B, A)

class A:
    def __init__(self):
        print("Метод класса А")

class B:
    def __init__(self):
        print("Метод класса B")

class C(B, A):
    def __init__(self):
        print("Метод класса C")

c = C()

# class C(B, A):
#     pass
#
# c = C()

Атрибут __mro__ (Method Resolution Order) - это порядок
в котором Python ищет методы в иерархии классов при наследовании. (C3)

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

print(D.__mro__)

class PC:
    a = 10

class Notebook:
    a = 20

class Nintendo:
    a = 30

class PlayStation(Notebook, PC, Nintendo):
    a = 40

test = PlayStation()
print(test.a)

Множественное наследование и super()

class A:
    def method(self):
        print("Метод класса А")

class B:
    def method(self):
        print("Метод класса B")

class C:
    def method(self):
        print("Метод класса C")

class D(A, B, C):
    def all_method(self):
        super(D, self).method() #можно заменить на super().method()
        super(A, self).method()
        super(B, self).method()
        # super(C, self).method() не нужно писать

d = D()
d.all_method()

Инкапсуляция пример про пульт - скрытие фкнкций.
Один из приницпов (ООп) который позволяет ограничить доступ к атрибутам или методам класса.
Благодаря такому подходу злоумышленники или же мы с вами не сможем
случайно или намерено вызвать или изменить чтобы либо в классе

Принципы инкапсуляции
!) Сокрытие данных. - скрывать данные от прямого пользоваться
 с помощью public, protected, private.
2) Методы доступа (геттеры и сеттеры) Нужны потому что нельяз напрямую
взаимодветсвовать с атрибутами и объектами
3) декораторы ( @property)

#public
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print(f'{self.name} - {self.age} years old.')

id1 = Person('Vasya', 18)
id1.print_data()
print(id1.name, id1.age)


"protected _ - не защищает, а обозначает что эти даынные нужно защищать"

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def print_data(self):
        print(f'{self._name} - {self._age} years old.')

id1 = Person('Vasya', 18)
id1.print_data()
print(id1._name, id1._age)

class Person:
    #защищеннный метода
    def _vasya_cat(self):
        print('Васин кот любит царапать диван ...')
    # публичный метод который помогает выводить инфо из защищенного метода
    def print_protected_method(self):
        self._vasya_cat()

id1 = Person()
id1.print_protected_method()

Private (приватные) атрибуты

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

account = BankAccount(1500)
#print(account.__balance())
print(account.get_balance())

class Person:
    #приватный метод
    def __vasya_cat(self):
        print('Васин кот любит царапать диван ...')
    # публичный метод который помогает выводить инфо из приватного метода
    def print_private_method(self):
        self.__vasya_cat()

id1 = Person()
id1.print_private_method()

Private и __dict__

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

account = BankAccount(1500)
print(account.__dict__)
print(account._BankAccount__balance)

Использование этих методов не является

class Bank:
    def __init__(self, name, bank_card, balance):
        self.__name = name
        self.__bank_card = bank_card
        self.__balance = balance
    def print_balance(self):
        print(f'Баланс карты {self.__balance}.')

    def change_money(self, money):
        if money < 0:
            print(self.__balance + money) # т.к. сразу вводим отрицательное занчение

        else self.__balance <= 0:
                print(f"Средств не достаточно")

# b = Bank("Vasya", "2200 1234 5678 9010", 1500)
# b.print_balance()
b.change_money(-100)
b.print_balance()
b.change_money(100)
b.print_balance()

Декоратор property (getter, setter, deleter)


class Person:
    def __init__(self, name):
        self.__name = name
# c посощью свойства геттер дос таем, хотя оно и неявно тут
    @property
    def name(self):
        return self.__name

person = Person('Vasya')
print(person.name)


class Person:
    def __init__(self, name):
        self.__name = name
# c посощью свойства геттер дос таем, хотя оно и неявно тут
    @property
    def name(self):
        return self.__name
#сеттер позволяет изменить приватный атрибут
    @name.setter
    def name(self, value):
        self.__name = value

person = Person('John')
print(person.name)

person.name = 'Vasya'
print(person.name)


class Person:
    def __init__(self, name):
        self.__name = name
# c посощью свойства геттер дос таем, хотя оно и неявно тут
    @property
    def name(self):
        return self.__name
#сеттер позволяет изменить приватный атрибут
    @name.deleter
    def name(self):
        del self.__name

person = Person('John')
print(person.__dict__)
del person.name
print(person.__dict__)
"""
class MagicBank:
    def __init__(self, account, balance):
        self.__account = account
        self.__balance = balance

    @property
    def happy_balance(self):
        return self.__balance

    @happy_balance.setter
    def happy_balance(self, value):
        self.__balance = value

    @happy_balance.deleter
    def value(self):
        self.__balance = 0


id_1 = MagicBank('Машенька', 500)
print(id_1.happy_balance)
id_1.happy_balance = 1000
print(id_1.happy_balance)

del id_1.happy_balance
print(id_1.happy_balance)
