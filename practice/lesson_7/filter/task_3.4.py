"""
 3. Задачи на функцию filter
* Напишите свою реализацию функций my_filter, возвращающую список.
"""


def my_filter(function, iterable):
    return [i for i in iterable if function(i)]


evens_only = my_filter(lambda a: a % 2 == 0, [1, -2, 3, -4, 0])
print(evens_only)
