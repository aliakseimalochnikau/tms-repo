"""
4. Задачи на функцию reduce
Дан список чисел. Найти его сумму.
"""


from functools import reduce


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


min_number = reduce(lambda x, y: min(x, y), input_list())
print(min_number)
