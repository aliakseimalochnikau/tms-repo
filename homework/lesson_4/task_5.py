"""
* Пользователь вводит произвольное число. Посчитайте сумму цифр этого числа используя операторы % и //
"""

num = num_to_print = int(input("Enter a number... "))  # Additional variable used in printing
sum_of_digits = 0

while num != 0:
    sum_of_digits += num % 10
    num //= 10
print(f"Sum of digits for number {num_to_print} is {sum_of_digits}.")
