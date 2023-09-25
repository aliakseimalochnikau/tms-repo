"""
* Напишите функцию get_most_frequent_word, которая на вход принимает текст (только английские слова и пробелы),
и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.
"""


def get_most_frequent_word(text: str) -> str:
    words = text.split()
    most_frequent_word = ''
    times_used = 0
    for word in words:
        if words.count(word) > times_used:
            times_used = words.count(word)
            most_frequent_word = word
    return most_frequent_word


text_fragment = 'hello this is a string with words and spaces and big big woooooooooord and and and'

assert(get_most_frequent_word(text_fragment)) == 'and'
