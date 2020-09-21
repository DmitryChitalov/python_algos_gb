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


def password_check():
    user_name = 'ilia'
    password = pbkdf2_hmac(hash_name='sha256',
                           password=input('enter ur password: ').encode(),
                           salt=user_name.encode(),
                           iterations=100000)
    print(hexlify(password))
    confirmation = pbkdf2_hmac(hash_name='sha256',
                               password=input('enter ur password again: ').encode(),
                               salt=user_name.encode(),
                               iterations=100000)
    print(hexlify(confirmation))
    if password == confirmation:
        return print('correct password')
    return print('incorrect password'), password_check()


password_check()
