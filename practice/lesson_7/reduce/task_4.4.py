"""
4. Задачи на функцию reduce
С помощью функции reduce и range найти факториал числа 5.
"""


from functools import reduce


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


factorial_5 = reduce(lambda x, y: x * y, range(1, 6))
print(factorial_5)
