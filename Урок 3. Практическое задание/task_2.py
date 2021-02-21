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

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""

from binascii import hexlify
from hashlib import pbkdf2_hmac


class User:
    __login: str
    __password_hash: str

    @staticmethod
    def register(login: str, password: str) -> 'User':
        # проверку на существования пользователя в виду ограниченности времени на ДЗ опускаем
        new_user = User()
        new_user.__login = login
        new_user.__password_hash = new_user.get_password_hash(password)
        print(new_user.__password_hash)  # делаем потому что это просится в условии задачи, в реальности конечно
        # записали бы в базу.
        return new_user

    def authorize(self, password: str):
        if self.__password_hash == self.get_password_hash(password):
            print('Пользователь авторизован')
            return True
        else:
            print('Ошибка авторизации')
            return False

    def get_password_hash(self, password: str):
        return hexlify(pbkdf2_hmac(hash_name='sha256', password=password.encode(),
                                   salt=self.__login.encode(), iterations=100000))


user = User.register(input('Введите логин > '), input('Введите пароль > '))
while not user.authorize(input('Введите пароль для авторизации > ')):
    continue

# P.S. на усложнение задачи нет времени.
