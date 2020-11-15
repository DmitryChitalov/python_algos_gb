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

def passwd_to_hash(pswd):
    return hashlib.sha256(salt.encode() + pswd.encode()).hexdigest()


salt = uuid4().hex
password = input('Введите пароль: ')
pswd_hash = passwd_to_hash(password)
print('Hash - ', pswd_hash)
password_confirmation = input('Введите пароль еще раз: ')
pswd_conf_hash = passwd_to_hash(password_confirmation)
print('Hash - ', pswd_conf_hash)

if pswd_hash == pswd_conf_hash:
    print('Пароль успешно подтвержден')
else:
    print('Пароли не совпадают')
