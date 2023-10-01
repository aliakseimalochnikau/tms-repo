"""
Пользователь вводит произвольное количество слов через пробел.
Затем (на следующей строке) вводит один символ (разделитель).
Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить,
и возвращает строку, в которой все слова из списка соединены через символ разделитель.
Используйте функцию reduce.
"""

# Solution 1: reduce() function
from functools import reduce

user_input = input('Enter a string of words separated by a space: ').split()
separator = input('Enter a separator: ')


def my_join(text, sep):
    return reduce(lambda x, y: x + f'{sep}' + y, text)


print(my_join(user_input, separator))


# Solution 2: join() function

user_input = input('Enter a string of words separated by a space: ').split()
separator = input('Enter a separator: ')
print(separator.join(user_input))
