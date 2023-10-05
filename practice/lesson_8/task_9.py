"""
Запишите свои данные в файл file_09.xlsx в формате Excel.
"""

import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Gender'
sheet['A2'] = 'Aliaksei'
sheet['B2'] = 'Malochnikau'
sheet['C2'] = 'M'

wb.save('file_09.xlsx')
