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

# from uuid import uuid4
# import hashlib
#
# salt = uuid4().hex
# bd = {}
# password1 = input('Введите пароль: ')
# print(hashlib.sha256(salt.encode() + password1.encode()).hexdigest())
# bd[password1] = hashlib.sha256(salt.encode() + password1.encode()).hexdigest()
# password2 = input('Введите пароль: ')
# print(hashlib.sha256(salt.encode() + password2.encode()).hexdigest())
# if hashlib.sha256(salt.encode() + password2.encode()).hexdigest() == bd[password1]:
#     print('Вы ввели правильный пароль')
# else:
#     print('Пароль не верен')


from hashlib import pbkdf2_hmac
from uuid import uuid4

salt = uuid4().hex
bd = {}
password1 = input('Введите пароль: ')
obj = pbkdf2_hmac(hash_name='sha256',
                  password=bytes(password1.encode()),
                  salt=bytes(salt.encode()),
                  iterations=100000)

print(obj)
bd[password1] = obj
password2 = input('Введите пароль: ')
obj2 = pbkdf2_hmac(hash_name='sha256',
                   password=bytes(password2.encode()),
                   salt=bytes(salt.encode()),
                   iterations=100000)
if obj2 == bd[password1]:
    print('Вы ввели правильный пароль')
else:
    print('Пароль не верен')
