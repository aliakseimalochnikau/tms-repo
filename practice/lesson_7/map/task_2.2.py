"""
2. Задачи на функцию map
Дан список чисел. Преобразуйте этот список в список строк.
"""


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


my_str_list = list(map(str, input_list()))
print(my_str_list)
