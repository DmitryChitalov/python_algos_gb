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

from uuid import uuid4
import hashlib


def authorization(hex_dig_res='', salt=''):
    # проверка на первый вход
    if hex_dig_res == '':
        user_pass = input('Введите пароль: ')
        salt = uuid4().hex
        user_pass_hash = hashlib.sha256(salt.encode() + user_pass.encode())
        hash_obj = user_pass_hash.hexdigest()
        print(hash_obj)
        # передаём соль, для повторной проверки
        return authorization(hash_obj, salt)
    else:
        user_pass = input('Введите пароль ещё раз: ')
        user_pass_hash = hashlib.sha256(salt.encode() + user_pass.encode())
        print(user_pass_hash.hexdigest())

        if hex_dig_res == user_pass_hash.hexdigest():
            print('Successfully')
            return True
        else:
            print('Collapse')
            return False


if __name__ == '__main__':
    entrance = authorization()