"""
Прочитайте файл из прошлого задания и выведите данные в формате "{Фамилия} {Имя} {Возраст}"
"""

import json

with open('file_04.json') as file:
    data = json.load(file)
    print(data)