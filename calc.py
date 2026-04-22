def add(num1: float, num2: float) -> float:
    return num1 + num2

def sub(num1: float, num2: float) -> float:
    return num1 - num2

def mul(num1: float, num2: float) -> float:
    return num1 * num2

def div(num1: float, num2: float) -> float:
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Не забываем на 0 делить нельзя')

"""
# или второй вариант проверки деления на ноль через условие
def div(num1: float, num2: float) -> float:
if num2 == 0:
    return 'деление на 0'
return num1 / num2
    """

