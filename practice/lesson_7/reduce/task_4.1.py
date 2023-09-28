"""
4. Задачи на функцию reduce
Дан список чисел. Найти его сумму.
"""


from functools import reduce


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


list_sum = reduce(lambda x, y: x + y, input_list())
print(list_sum)
