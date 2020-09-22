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

hash_db = b'5ddcce9b50adbd4b57414eeca9c10b41bd9afc4125556d1895aa9f2c9eae67ef'  # хеш пароля 123 в базе данных
user_name = b'John@gmail.com'  # логин пользователя, считаем уникальным
user_pass = input('Enter your password : ')
get_pass_hash = pbkdf2_hmac(hash_name='sha256',
                            password=user_pass.encode(),
                            salt=user_name,
                            iterations=10000)
print(f'Hash in database      : {hash_db}')
print(f'Hash of your password : {hexlify(get_pass_hash)}')
if hash_db == hexlify(get_pass_hash):
    print(f'Your password is right')
else:
    print(f'Your password is incorrect')