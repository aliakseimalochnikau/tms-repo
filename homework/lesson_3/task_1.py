"""
Пользователь вводит одно число, сторона квадрата.
Вывести кортеж из трёх чисел: периметр квадрата, площадь квадрата, диагональ квадрата.
"""

side = int(input('Enter the side length of the square...'))
perimeter = side * 4
area = side ** 2
diagonal = (2 * side ** 2) ** 0.5
print((perimeter, area, diagonal))
