"""
 3. Задачи на функцию filter
 Дан список чисел. Выведите три числа: количество положительных чисел, количество нулей
 и количество отрицательных чисел. Используйте функции filter и len.
"""


def input_list(prompt='', sep=' ', element_type=int):
    return [element_type(s) for s in input(prompt).split(sep)]


my_list = input_list()

positive_count = len(list(filter(lambda x: x > 0, my_list)))
negative_count = len(list(filter(lambda x: x < 0, my_list)))
zero_count = len(list(filter(lambda x: x == 0, my_list)))

print(positive_count, negative_count, zero_count)
