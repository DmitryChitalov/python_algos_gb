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

from hashlib import pbkdf2_hmac
from binascii import hexlify

salt = b'login123'
pass_input1 = input('введите пароль:')

hash_obj = pbkdf2_hmac(hash_name='sha256',
                         password=pass_input1.encode(),
                         salt=salt,
                         iterations=100000)

pass_result1 = hexlify(hash_obj)
print (f'сохраненный hash пароля:{pass_result1}')

pass_input2 = input('повторите пароль:')

hash_obj2 = pbkdf2_hmac(hash_name='sha256',
                         password=pass_input2.encode(),
                         salt=salt,
                         iterations=100000)

pass_result2 = hexlify(hash_obj2)

if pass_result1 == pass_result2:
    print('пароль подтвержден')
else:
    print('введены разные пароли')
