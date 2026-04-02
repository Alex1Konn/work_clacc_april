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