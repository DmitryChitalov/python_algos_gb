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

login_request = 'ID1'

password_request = str(input("Password: "))

hash_obj_str = hashlib.sha256(login_request.encode('utf-8') + password_request.encode('utf-8')).hexdigest()

print(hash_obj_str)

password_request = str(input("Input Password one more time: "))

hash_obj_str_check = hashlib.sha256(login_request.encode('utf-8') + password_request.encode('utf-8')).hexdigest()

if hash_obj_str == hash_obj_str_check:
    print('Password is correct')
else:
    print('Password is not correct')
