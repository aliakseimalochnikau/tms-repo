"""
2. Задачи на функцию map
Дан список чисел. Увеличьте каждый элемент в 100 раз.
"""


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


my_list_100 = list(map(lambda x: x * 100, input_list('Enter numbers: ', sep=',')))
print(my_list_100)

