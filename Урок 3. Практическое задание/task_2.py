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

import hashlib
import uuid


def get_hash(password, salt=False):
    if not salt:
        # Генерируем соль.
        salt = uuid.uuid4().hex
    # Получаем хеш.
    return hashlib.sha256(salt.encode() + password.encode() + salt.encode()).hexdigest() + salt


if __name__ == "__main__":
    password = input('[?] Введите пароль: ')
    # Получаем хеш.
    hash_with_salt = get_hash(password=password)
    print(f'[=] Созданный хеш: {hash_with_salt}')
    password_again = input('[?] Введите пароль еще раз для проверки: ')

    only_salt = hash_with_salt[-32:]
    if hash_with_salt == get_hash(password=password_again, salt=only_salt):
        print('[v] Пароли совпадают.')
    else:
        print('[x] Неверный пароль!')
