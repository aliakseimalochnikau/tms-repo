from random import randint


class User:
    def __init__(self, login, password):
        self.login = login
        self.__key = randint(1, 1000)
        self.__encoded_password = self.__encode(password)

    def __encode(self, s):
        return ''.join([chr(ord(i) ^ self.__key) for i in s])

    def check_password(self, password):
        return self.__encoded_password == self.__encode(password)

    def reset_password(self, new_password):
        self.__encoded_password = self.__encode(new_password)


my_user = User('dima_buevich', 'SuperSecretP@ssword')

print(my_user.login)
# print(my_user.__password)  # так нельзя, будет ошибка

print(my_user.check_password('WrongPassword'))
print(my_user.check_password('SuperSecretP@ssword'))

my_user.reset_password('NewP@ssword')

print(my_user.check_password('SuperSecretP@ssword'))
print(my_user.check_password('NewP@ssword'))
