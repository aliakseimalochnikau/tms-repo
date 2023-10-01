"""
Пользователь вводит произвольное количество маленьких латинских букв через пробел.
Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
Выведите результат работы на экран.

"""

s = input('Enter a string of chars separated by a space... ').lower().split()


def remove_vowels(lst):
    return list(filter(lambda x: x not in 'aeiouy', lst))


print(remove_vowels(s))
