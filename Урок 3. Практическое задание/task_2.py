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


def authentication():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    password_hash = hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()
    with open('hash_password.txt', 'w', encoding='utf-8') as f1:
        f1.write(password_hash)
    repeat_password = input('Пожалуйста введите пароль ещё раз: ')
    repeat_password_hash = hashlib.sha256(login.encode('utf-8') + repeat_password.encode('utf-8')).hexdigest()
    with open('hash_password.txt', 'r', encoding='utf-8') as f2:
        if f2.read() == repeat_password_hash:
            return 'Доступ предоставлен'
        else:
            return 'В доступе отказано'


print(authentication())