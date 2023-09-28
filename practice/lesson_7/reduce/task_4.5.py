"""
4. Задачи на функцию reduce
* Напишите свою реализацию функции my_reduce. Для простоты можно сделать третий параметр обязательным.
"""


def my_reduce(function, iterable, initializer):
    result = initializer
    for element in iterable:
        result = function(result, element)
    return result


product = my_reduce(lambda x, y: x + y, [2, 3, 4, 5], 0)
print(product)
