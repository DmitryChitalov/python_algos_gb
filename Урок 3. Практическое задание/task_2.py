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

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""

import hashlib
from uuid import uuid4

password = input('Input password: ')
password_re = input('Reinput password: ')

# 1

# salt = uuid4().hex  # здесь генерится 16-ричное представление с типом str
# """Здесь соль и пароль кодируются в байты, складываются и ?декодируются? в 16-ричное представление с типом str"""
# hash_obj = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
# print(hash_obj)
#
# salt_re = uuid4().hex
# hash_obj_re = hashlib.sha256(salt.encode() + password_re.encode()).hexdigest()
# print(hash_obj_re)
#
# if hash_obj == hash_obj_re:
#     print("Вы ввели правильный пароль")

# 2

salt = uuid4().hex
hashfunc = hashlib.sha256


def hash_pass(password, salt, hashfunc):
    result = hashfunc(password.encode() + salt.encode()).hexdigest()
    return result, print(result)


a = hash_pass(password, salt, hashfunc)
b = hash_pass(password_re, salt, hashfunc)

i = 0
while i < 3:
    if a == b:
        print("Вы ввели правильный пароль")
        break
    else:
        i += 1
        print("Вы ввели НЕправильный пароль")
        password_re = input('Reinput password: ')
        b = hash_pass(password_re, salt, hashfunc)
        if i >= 3:
            print("Превышено кол-во попыток")
