"""
Прочитайте файл из прошлого задания и выведите данные в формате "{Фамилия} {Имя} {Возраст}".
"""

import csv

with open('file_07.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
