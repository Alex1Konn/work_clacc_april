"""
Модуль  accessify - это библиотека python, которая позволяет создавать
приватные и защищенные методы используя декораторы.
Библиотеку необходимо импортировать и установить.
Декораторы - аналогии тетрадь с запахом, пистолет с глушителем
Это более явный способ защиты данных, чем просто декораторы
@private
@protected

from accessify import private

class MyClass:
    a = 2
    b = 3

    @private
    def private_sum_ab(self):
        print(f"{self.a + self.b}")

    def public_sum_ab(self):
        self.private_sum_ab()

obj = MyClass()
obj.public_sum_ab()
obj.public_sum_ab()


from accessify import protected

class MyClass:
    @protected
    def _protected(self):
        print("Это защищенный метод")

    def _public(self):
        self._protected()

obj = MyClass()
obj._public()
obj.protected()

Исключения в python это специальные объекты, которые возникают в процессе выполнения программы,
когда происходит ошибка.
В python исключения являются классамии и в них существует наследования.
Для эффективной работы с исключениями важно понимать порядок наследования исключений.

try:
    b = 3 / 0
    a = 11
#проверка на конкретную ошибку есть или нет
except ZeroDivisionError:
    print("ZeroDivisionError")
----------------
try:
    #возникает ошибка деления на ноль ZeroDivisionError
except ValueError:
    #код который обрабатывает исключние ValueError

except ZeroDivisionError:
# код который обрабатывает исключние ZeroDivisionError
except:
    #Код который обрабатывает все исключения
"""
"""
Разбор примеров try-except

#ZeroDivisionError
try:
    x = int(input())
    y = int(input())
    z = x / y

except ZeroDivisionError:
    print("Деление на ноль")

#ValueError - Аргумент правильногог типа, но неверного значения
try:
    number = int("Qwerty")
except ValueError:
    print("Ошибка, переменная number не число")

#IOError при возникновении ввода\вывода,
#файл защищенный от записи или поиск по имени файла которого не существует
try:
    f = open("file.txt")

except IOError:
    print("Ошибка открытия файла")

#except as
try:
    x = 1 / 0

except Exception as p:
    print(p, type(p))

использование исключенией помогает быстро найти ошибки в коде, а не останвоить работу программу

try:
    x = 1 / 'Vasya'

except:
    print(f"Ошибка в переменной {x}")

class BeautyTransform:
    def __init__(self, height, weight=0):
        self.height = height
        self.weight = weight

    def transformer(self):
        try:
            new_body = self.height / self.weight
            print("Успешная трансформация")

        except ZeroDivisionError:
            print("Лицо как в картине Крик, Эдварда Мунка")

id1 = BeautyTransform(169, 85)
id1.transformer()

id2 = BeautyTransform(169,)
id2.transformer()

try:
    x = 1 / 0
except Exception as error:
    print(f"Возникла ошибкаЖ {error} {type(error)}")

try:
    x = 1 / 0
except ArithmeticError as error:
    print(f"Возникла ошибка {error} {type(error)}")
_____________________
#вариант 1
try:
    x = 1 / 0
except Exception as error:
    print(f"Возникла ошибка {error} {type(error)}")
#вариант 2
try:
    x = 1 / 0
except ZeroDivisionError as error:
    print(f"Возникла ошибка {error} {type(error)}")
"""
"""
try-except-else-finally
finelly - блок выполянеятся всегда при любыху словиях

try:
    x = int("42")

except ValueError:
    print("Ошибка преобразования типа")
else:
    print("x =", x)

try:
    f = open("file.txt", 'w')
finally:
    f.close()
    print("Блок finally отработал")

try:
    x = int("42")
except ValueError:
    print("ОШибка преобразования типа")
else:
    print("x =", x)
finally:
    print("конец прогнраммы")
"""

"""
Вложенные try-except

try:
    x = int(input())
    y = int(input())
    try:
        z = x / y
    except ZeroDivisionError as zero:
        z = zero
except Exception as ex:
    print(ex)
else:
    print(z)
"""
class BeautyTransform:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.result = "Божественная красота"

    def transformer(self):
        try:
            new_body = self.height / self.weight

        except Exception:
            self.result = "Индюк на 3 дня"
        else:
             print("Проверка прошла", end='')
        finally:
            print(self.result)

vasya = BeautyTransform(169, 85)
vasya.transformer()