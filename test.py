__all__ = ['func', 'MyClass', 'number']

number = 35  #Не экспортируется

def func():   #Экспортируемся
    print('Hello')

class MyClass:  # Экспортируется
    a = 10

import April_22

def func_b():
    April_22.func_a()

class Child(April_22.Base):
    pass