"""
Напишите функцию-декоратор my_decorator, в которую можно обернуть функцию, которая принимает один входной параметр.
Ваш декоратор должен будет выводить в консоль входной параметр оборачиваемой функции, запускать функцию,
а затем выводить результат этой функции.

"""

from functools import reduce


def my_decorator(function):
    def find_factorial_extended(num):
        print(f'Функция получила на вход значение {num}')
        print(f'Результат функции: {function(num)}')
        return function(num)

    return find_factorial_extended


@my_decorator
def find_factorial(num):
    return reduce(lambda x, y: x * y, range(1, num + 1))


factorial = find_factorial(5)
print(f'factorial = {factorial}')
