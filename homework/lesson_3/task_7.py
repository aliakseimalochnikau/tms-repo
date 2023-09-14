"""
* Пользователь вводит число, выведите True если оно простое, иначе False
"""

num = int(input("Enter a number..."))
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
        break
print(flag)
