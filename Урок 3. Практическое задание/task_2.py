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
import random

salt = str(random.randint(100 , 999))
print('Соль хэша - ', salt)
hpass = hashlib.sha256(input(' Введите пароль').encode() + salt.encode())

print(f'Хэш введенного пароля - {hpass.hexdigest()}:{salt}')

hpass2 = hashlib.sha256(input(' Введите пароль еще раз').encode() + salt.encode())
print(f'Хэш введенного пароля - {hpass2.hexdigest()}:{salt}')


if hpass.hexdigest() == hpass2.hexdigest():
    print('Пароль введен верно')
else:
    print('Пароль введен не верно')


# c7555c52934ca57677cbbf9df741e462e75a942d57de1b52a8176643e609fd2a