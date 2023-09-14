"""
Пользователь вводит месяц и число. Выведите True, если такой день есть в году.
"""
calendar = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
month = input("Enter a month...")
day = int(input("Enter a day..."))
print(month in calendar and 0 < day <= calendar[month])
