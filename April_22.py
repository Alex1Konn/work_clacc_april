"""
НАПИСАНИЕ МОДУЛЕЙ
"""
# import random
# print(random.randint(1,10))

# import random as r
# print(r.randint(1,10))

# from random import randint
# print(randint(1,10))

# from random import randint, choice
# print(randint(1,10))
# print(choice([1,2,3,4,5]))

# from random import randint as rint, choice as ch
# print(rint(1,10))
# print(ch([1,2,3,4,5]))

# from math import pi
# print(pi)

#импорт всех функций
# from math import *
# print(pi)
# print(sqrt(pi))


"""
СОЗДАНИЕ СВОЕГО МОДУЛЯ
"""
# from test import func, MyClass, number
#
# func()
# print(number)
# print(MyClass.a)


# from test import *
#
# func()
#
# print(number)
#
# print(MyClass.a)

# без choice
# import random
# a = [1, 2, 3, 4]
#
# index = random.randint(0, len(a) - 1)
# rand_num = a[index]
#
# print(rand_num)

# аналог
# import random
# a = [1, 2, 3, 4]
# print(random.choice(a))


#ДВА МОДУЛЯ ИМПОРТИРУЮТ ДРУГ ДРУГА
# import test
#
# def func_a():
#     test.func_b()
#
# class Base:
#     pass

from calc import add, sub, mul, div
class Calculator:
    def __init__(self) -> None:
        self.main()

    def main(self):
        print('Это калькулятор')
        while True:
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
            choice = int(input('Выберите необходимое действие 1: +, 2: -, 3: *, 4: /, 0: Выход\n '))
            match choice:
                case 0:
                    print('Для заверешения нажмите Enter')
                    input()
                    break
                case 1:
                    print(add(num1, num2))
                case 2:
                    print(sub(num1, num2))
                case 3:
                    print(mul(num1, num2))
                case 4:
                    print(div(num1, num2))
                case _:
                    print('Неверный выбор')
obj = Calculator()
