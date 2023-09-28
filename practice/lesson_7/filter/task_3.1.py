"""
 3. Задачи на функцию filter
 Дан список чисел. Удалите из него отрицательные числа.
"""


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


positive_nums_only = list(filter(lambda x: x > 0, input_list()))
print(positive_nums_only)
