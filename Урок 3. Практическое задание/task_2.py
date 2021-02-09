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
import os
import hashlib
from binascii import hexlify

print('Enter password:')
v_pass = input()
salt = os.urandom(32)
v_key = hashlib.pbkdf2_hmac('sha256', v_pass.encode('utf-8'), salt, 100000)
v_pass_storage = salt + v_key
print(hexlify(v_pass_storage))
print('Re-enter password:')
v_2nd_pass = input()
v_check_key = hashlib.pbkdf2_hmac('sha256', v_2nd_pass.encode('utf-8'), v_pass_storage[:32], 100000)
print(hexlify(v_pass_storage[:32] + v_check_key))
if v_key == v_pass_storage[32:]:
    print('Passwords are equal')
else:
    print('Passwords are NOT equal')