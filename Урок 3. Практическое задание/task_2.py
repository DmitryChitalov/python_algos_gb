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

user_data_first = input('Введите пароль:   ').encode('utf-8')

# Здесь мы создаем хеш sha256 в пароле при помощи соли со 100,000 итераций.
obj = pbkdf2_hmac(hash_name='sha256',
                  password=user_data_first,
                  salt=b'any_salt_1',
                  iterations=100000)
obj = pbkdf2_hmac(hash_name='sha256',
                  password=user_data_first,
                  salt=b'any_salt_2',
                  iterations=100000)
print(f'В базе данных хранится строка: {hexlify(obj)}')


user_data_second = input('Введите пароль еще раз для проверки:   ').encode('utf-8')
obj_2 = pbkdf2_hmac(hash_name='sha256',
                    password=user_data_second,
                    salt=b'any_salt_1',
                    iterations=100000)
obj_2 = pbkdf2_hmac(hash_name='sha256',
                    password=user_data_second,
                    salt=b'any_salt_2',
                    iterations=100000)
if hexlify(obj) == hexlify(obj_2):
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неправильный пароль')