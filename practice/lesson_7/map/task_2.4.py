"""
2. Задачи на функцию map
* Напишите свою реализацию функций my_map, возвращающую список.
"""


def my_map(function, iterable):
    return [function(i) for i in iterable]


squares = my_map(lambda a: a + 100, [1, 2, 3, 4])
print(squares)
