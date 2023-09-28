"""
 3. Задачи на функцию filter
** Напишите свою реализацию функций my_filter, которая вместо возвращения списка
использует ключевое слово yield при генерации очередного элемента.
"""


def my_filter(function, iterable):
    for element in iterable:
        if function(element):
            yield element


two_and_more = list(my_filter(lambda s: len(s) > 1, ['a', 'bb', 'ccc']))
print(two_and_more)
