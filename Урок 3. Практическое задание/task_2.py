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


def autorization(password,
                 n=0,
                 password_hash=0,
                 password_hash_new=0,
                 salt='1585'):
    if n == 1:
        password = input('Введите пароль еще раз для проверки: ')
        password_hash_new = hashlib.sha256(
            password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        if password_hash == password_hash_new:
            return f'Вы ввели правильный пароль'
        else:
            print('Пароль не верный!')
            return autorization(password, n, password_hash, password_hash_new,
                                salt)
    elif n == 0:
        password_hash = hashlib.sha256(
            password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        print(f'В базе данных хранится строка: {password_hash}')
        return autorization(password, n + 1, password_hash, password_hash_new,
                            salt)


print(autorization(input('Введите пароль: ')))