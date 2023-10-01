"""
* Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
Вам по прежнему нужно удалить все гласные. При этом результат нужно вывести, сохранив изначальный регистр.
"""

s = input('Enter a string of chars separated by a space... ').split()

def remove_vowels(lst):
    return list(filter(lambda x: x not in 'AaEeIiOoUuYy', lst))


print(remove_vowels(s))
