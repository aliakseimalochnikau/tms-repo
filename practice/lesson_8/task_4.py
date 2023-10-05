"""
Пользователь вводит свои данные (имя, фамилия, возраст). Запишите эти данные в файл file_04.json формате JSON.
"""

import json

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

data = {
    'name': name,
    'surname': surname,
    'age': age
}

with open('file_04.json', 'w') as file:
    json.dump(data, file)
