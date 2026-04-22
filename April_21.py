"""

декораторы

#Функция как объект
def greet(name):
    return f"Hello, {name}!"

my_func = greet
print(my_func("ИМЯ"))

#Замыкание - это прототип декоратора, где есть функция и к не добавляем еще один функционал
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(10))
# явный декоратор
def my_decorator(func):
    def wrapper():
        print("Что-то  происходит ПЕРЕД выховом функции")
        func()
        print("Что-то происходит ПОСЛЕ выхова функции")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")
say_hello()

#Эквивалент без синтаксиса @

def my_decorator(func):
    def wrapper():
        print("Что-то  происходит ПЕРЕД выховом функции")
        func()
        print("Что-то происходит ПОСЛЕ выхова Функции")
    return wrapper

def say_hello():
    print("Hello, world!")
say_hello = my_decorator(say_hello)
say_hello()


#Декораторы для функций с аргументами
# func.__name__ будет подменяться на названии функции
def smart_divide(func):
    def wrapper(*args):
        print(f" Вызывается функция {func.__name__} с аргументами {args}")
        result = func(*args)
        print(f"Результат: {result}")
        return result
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

divide(10, 2)

def salary_net(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Зарплата на руки: {result}")
        return result
    return wrapper
@salary_net
def salary_gross(a):
    return a - (a/100*13)

salary_gross(10000000)


#декораторы с параметрами

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("World")

#Несколько декораторов

def decorator1(func):
    def wrapper():
        print("Декоратор 1 - до")
        func()
        print("Дектор 1 - после")
    return wrapper

def decorator2(func):
    def wrapper():
        print("декоратор 2 - до")
        func()
        print("декоратор 2 - после")
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Основная функция")

my_function()
"""
#
# def my_decotator(func):
#     def wrapper():
#         """Документация wrapper"""
#         return func()
#     return wrapper
# @my_decotator
# def original_func():
#     """Документация original_func"""
#     pass
#
# print(original_func.__name__) #wrapper
# print(original_func.__doc__) #Документация wrapper
#
# from functools import wraps
#
# def my_decotator(func):
#     @wraps(func)
#     def wrapper():
#         """Документация wrapper"""
#         return func()
#     return wrapper
#
# @my_decotator
# def original_func():
#     """Документация original_func"""
#     pass
#
# print(original_func.__name__) # original_func
# print(original_func.__doc__) #Документация wrapper
"""
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнялась {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Готово!"
slow_function()
# задача с измерением декоратором алгоритма
import time
from functools import wraps
import random

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнялась {end_time - start_time:.4f} секунд")
        return result
    return wrapper

arr = random.sample(range(1, 10001),10000)

@timer
def shell_sort(arr):
  n = len(arr)
  gap = n // 2

  while gap > 0:
    for i in range(gap, n):
      temp = arr[i]
      j = i
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap
      arr[j] = temp
    gap //=2
  return arr

print(shell_sort(arr))
target = 4000

def linear_search(arr, target):
  for k, item in enumerate(arr):
    if item == target:
      return k
  return -1

result = linear_search(arr, target)
print(f'Элемент {target} найден на позиции {result}' if result != -1 else f"Элемент {target} не найден")

# for _ in range(1000000):
#     pass
"""
#1

# def logger(func):
#     def wrapper(*args):
#         print(f" Вызывается функция {func.__name__} с аргументами {args}")
#     return wrapper
#
# @logger
# def my_logger(a, b):
#     return a + b
#
# my_logger(10, 20)

#3
"""
def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        for _ in range(count):
            count += 1
            result = func(*args, **kwargs)
            return f'Счетчик {count} функция {result}'
        return wrapper
    return call_counter

@call_counter
def say_hello(name):
    print(f"Hello, {name}!")
    return name

say_hello("Иван")
say_hello("Мария")
print(say_hello("Петр"))


def call_counter(num_times): # Теперь передаем количество повторов
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(num_times):
                res = func(*args, **kwargs)
                results.append(f"Вызов {i + 1}: {res}")
            return "\n".join(results)
        return wrapper
    return decorator

@call_counter(3) # Указываем, сколько раз запустить функцию
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("ИМЯ"))
"""

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n=3)
def print_hello():
    print("Hello")

print_hello()
