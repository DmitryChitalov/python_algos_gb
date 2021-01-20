"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
from hashlib import sha256


class Login:
    def __init__(self):
        self.password = None

    def new_password(self):
        user_password = input('Введите новый пароль:\n')
        self.password = sha256(user_password.encode('utf-8')).hexdigest()

    def password_check(self):
        while True:
            user_password = input('\nВведите пароль:\n')
            if self.password == sha256(user_password.encode('utf-8')).hexdigest():
                print('Вы вошли')
                break
            else:
                print('Вы ввели неправильный пароль')


user = Login()
user.new_password()
user.password_check()
