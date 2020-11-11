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
from hashlib import pbkdf2_hmac
from binascii import hexlify


class UserLogin:
    def __init__(self):
        self.user = str()
        self.pwd = str()

    @staticmethod
    def _check_in_user(user, pwd):
        """
        Метод осуществляет соленое хэширование пароля
        """
        obj = pbkdf2_hmac(hash_name='sha256',
                          password=pwd.encode('utf8'),
                          salt=user.encode('utf8'),
                          iterations=100000)
        return hexlify(obj)

    def check_pwd(self):
        """
        Метод запрашивает данные юзера, записывает их в бд, при этом вместо пароля в бд записывается хзш.
        Далее идет повторная проверка пароля сравниванием хэш-ей.
        """
        self.user = input('Введите логин: ')
        self.pwd = input('Введите пароль: ')
        storage = {'login': self.user, 'pwd': self._check_in_user(self.user, self.pwd)}
        if self._check_in_user(self.user, input('Введите пароль повторно: ')) == storage.get('pwd'):
            print('Вы ввели правильный пароль!')
        else:
            print('Вы ввели ошибочный пароль!')


user = UserLogin()
user.check_pwd()
