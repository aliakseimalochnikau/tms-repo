"""
Пользователь вводит произвольное количество латинских букв через пробел.
Буквы могут быть как в верхнем, так и в нижнем регистре (на результат работы это влиять не должно).
Напишите функцию map_to_tuples, которая принимает список из этих букв и возвращает список из кортежей.
В каждом кортеже первой должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
Выведите результат работы функции на экран.
"""


my_list = input('Enter a string of chars separated by a space... ').split()


def map_to_tuples(lst):
    return list(map(lambda x: (x.upper(), x.lower()), lst))


print(map_to_tuples(my_list))
