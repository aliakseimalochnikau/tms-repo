"""
Вывести на экран числа кратные 5 от 0 до 100 включительно.
1.1. Сделать это с помощью функции range с шагом 5
1.2. Сделать это с помощью функции range c шагом 1 и вложенным if
"""

# 1.1.
for i in range(0, 101, 5):
    print(i, end=' ')  # using 'end' to print numbers in line

print()  # used to start next solution from a new line

# 1.2.
for i in range(101):
    if i % 5 == 0:
        print(i, end=' ')  # using 'end' to print numbers in line
