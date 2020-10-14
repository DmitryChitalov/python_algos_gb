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

def pswd_check():
    pswd = input('Введите пароль:')
    salt = 'All you need is love'
    hash_hex_salt_pswd = hashlib.sha256(pswd.encode()+salt.encode()).hexdigest()
    print(hash_hex_salt_pswd)
    pswd_check = input('Введите еще раз пароль для проверки:')
    hash_hex_salt_pswd_check = hashlib.sha256(pswd_check.encode()+salt.encode()).hexdigest()
    print(hash_hex_salt_pswd_check)
    if hash_hex_salt_pswd == hash_hex_salt_pswd_check:
        return ('Пароль верный')
    else:
        return ('Неверный пароль')

print(pswd_check());