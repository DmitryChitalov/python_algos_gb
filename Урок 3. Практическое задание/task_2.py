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

from uuid import uuid4
passwd= input("введите пароль:")
salt = uuid4().hex


res = hashlib.sha256(salt.encode('utf-8') + passwd.encode('utf-8')).hexdigest()
print(res)

print()

pas_repeat=input("vvedite svoy parol povtorna")
res_new = hashlib.sha256(salt.encode('utf-8') +pas_repeat.encode('utf-8')).hexdigest()
if res_new==res:
    print('vi vveli pravilniy parol')
else:
    print("parol nepravilniy")