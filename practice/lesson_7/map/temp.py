from functools import reduce


def input_list(prompt="", sep=" ", element_type=int):
    return list(map(element_type, input(prompt).split(sep)))


# no_negative_list = list(filter(lambda x: x > 0, input_list()))
# print(no_negative_list)

# no_odd_list = list(filter(lambda x: x % 2 == 0, input_list()))
# print(no_odd_list)


# Дан список чисел. Найти его сумму.

# sum_list = reduce(lambda x, y: x + y, input_list())
# print(sum_list)

# Дан список чисел. Найти минимальное число.
# min_list = reduce(lambda x, y: min(x, y), input_list())
# print(min_list)

my_string = 'hello this is my string'
print('@'.join(my_string.split()))

# Дан список чисел. Найти произведение всех элементов.

