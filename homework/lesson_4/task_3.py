"""
Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
Если он ответил “yes” - завершите программу.
Если он ответил “no” - продолжайте - продолжайте вывод чисел.
Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор,
пока ответ не будет корректным.
"""


def check_answer(answer: str) -> str:
    while answer not in ('yes', 'no'):
        print("Don't understand you")
        answer = input("Should we break? ").lower()
    return answer


for i in range(101):
    print(i)
    user_input = input("Should we break? ").lower()
    user_answer = check_answer(user_input)
    if user_answer == 'yes':
        break
    else:
        continue

