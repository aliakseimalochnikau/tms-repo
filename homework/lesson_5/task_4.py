"""
Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.
"""


def get_longest_word(text: str) -> str:
    words = text.split()
    longest_word = ''
    max_chars = 0
    for word in words:
        if len(word) > max_chars:
            max_chars = len(word)
            longest_word = word
    return longest_word


text_fragment = 'hello this is a string with words and spaces and big big woooooooooord'

assert (get_longest_word(text_fragment)) == 'woooooooooord'