"""
4. Задачи на функцию reduce
Дан список чисел. Найти произведение всех элементов.
"""


from functools import reduce


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


product = reduce(lambda x, y: x * y, input_list(), 1)
print(product)
