"""
2. Задачи на функцию map
** Напишите свою реализацию функций my_map, которая вместо возвращения списка использует
ключевое слово yield при генерации очередного элемента.
"""


def my_map(function, iterable):
    for i in iterable:
        yield function(i)


upper = list(my_map(lambda s: s.upper(), ['a', 'b', 'c']))
print(upper)
