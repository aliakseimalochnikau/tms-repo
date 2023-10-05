"""
Пользователь вводит свои данные (имя, фамилия, возраст). Запишите эти данные в файл file_07.csv формате CSV.
"""

import csv

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

header = ('name', 'surname', 'age')
data = (name, surname, age)

with open('file_07.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerow(data)

