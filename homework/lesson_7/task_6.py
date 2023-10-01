"""
* Решите прошлую задачу так, чтобы ваш декоратор работал для любой функции, с любым количеством параметров.
А также чтобы работало с именованными параметрами.
Подсказка: используйте *args и **kwargs.
"""


def my_decorator(function):
    def new_function(*args, **kwargs):
        print(f'Функция получила на вход значение {args}, {kwargs}')
        print(f'Результат функции: {function(*args, **kwargs)}')
        return function(*args, **kwargs)

    return new_function


@my_decorator
def calculate_sum(a, b, c, d):
    return a + b + c + d


result = calculate_sum(1, 2, d=3, c=4)
print(f'sum = {result}')
