"""
2. Задачи на функцию map
Дан список чисел. Разделите каждый элемент на 100 и округлите до целого числа (функция round).
"""


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


my_list_round = list(map(lambda x: round(x / 100), input_list()))
print(my_list_round)
