"""
 3. Задачи на функцию filter
 Дан список чисел. Удалите из него нечётные числа.
"""


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


evens_only = list(filter(lambda x: x % 2 == 0, input_list()))
print(evens_only)
