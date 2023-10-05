"""
Запишите свои данные в файл file_06.csv в формате CSV.
Пример:
name,surname,gender
Dmitry,Buevich,M
"""

import csv

header = ('name', 'surname', 'gender')
data = ('Aliaksei', 'Malochnikau', 'M')

with open('file_06.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerow(data)
